import logging
import xml.etree.ElementTree as ET
from flask import Flask, jsonify, render_template
import requests

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

FEED_URL = "https://docs.cloud.google.com/feeds/bigquery-release-notes.xml"

def parse_atom_feed(xml_data):
    """
    Parses the Atom XML feed into a structured list of entries.
    """
    try:
        root = ET.fromstring(xml_data)
    except ET.ParseError as e:
        logger.error(f"XML parse error: {e}")
        return []

    # Atom namespace
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    
    entries = []
    for entry in root.findall('atom:entry', ns):
        title_el = entry.find('atom:title', ns)
        id_el = entry.find('atom:id', ns)
        updated_el = entry.find('atom:updated', ns)
        content_el = entry.find('atom:content', ns)
        link_el = entry.find('atom:link[@rel="alternate"]', ns)
        
        # Fallback if specific alternate link is not found
        if link_el is None:
            link_el = entry.find('atom:link', ns)
            
        title = title_el.text if title_el is not None else ""
        entry_id = id_el.text if id_el is not None else ""
        updated = updated_el.text if updated_el is not None else ""
        content = content_el.text if content_el is not None else ""
        link = link_el.attrib.get('href', '') if link_el is not None else ""
        
        entries.append({
            'id': entry_id,
            'title': title,
            'updated': updated,
            'content': content,
            'link': link
        })
        
    return entries

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/release-notes')
def get_release_notes():
    try:
        response = requests.get(FEED_URL, timeout=10)
        response.raise_for_status()
        xml_data = response.content
        entries = parse_atom_feed(xml_data)
        return jsonify({
            'success': True,
            'entries': entries
        })
    except requests.RequestException as e:
        logger.error(f"Error fetching BigQuery release notes: {e}")
        return jsonify({
            'success': False,
            'error': f"Failed to fetch release notes: {str(e)}"
        }), 500
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({
            'success': False,
            'error': "An unexpected error occurred."
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
