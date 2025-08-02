from jinja2 import Template

HTML_TEMPLATE = """
<h2>Broken Links & Misconfig Report</h2>
<p>Total URLs scanned: {{ total }}</p>
<p>Broken links: {{ broken|length }}</p>

<h3>Broken Links</h3>
<ul>
{% for item in broken %}
  <li>{{ item.url }} - Status: {{ item.status_code }}</li>
{% endfor %}
</ul>

<h3>Missing Headers</h3>
<ul>
{% for item in data %}
  {% if item.missing_headers %}
    <li>{{ item.url }}: Missing - {{ item.missing_headers|join(', ') }}</li>
  {% endif %}
{% endfor %}
</ul>

<h3>Directory Listing Enabled</h3>
<ul>
{% for item in data %}
  {% if item.directory_listing %}
    <li>{{ item.url }}</li>
  {% endif %}
{% endfor %}
</ul>
"""

def generate_html_report(data, filename="report.html"):
    broken = [d for d in data if d['broken']]
    tmpl = Template(HTML_TEMPLATE)
    html = tmpl.render(data=data, total=len(data), broken=broken)

    with open(filename, "w") as f:
        f.write(html)
    print(f"[+] HTML report saved as {filename}")

