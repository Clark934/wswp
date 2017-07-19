import lxml.html
broken_html = '<ul class=country><li>Area<Li>Population</ul>'
tree = lxml.html.fromstring(broken_html)
fixed_html = lxml.html.tostring(tree, pretty_print=True)
print fixed_html