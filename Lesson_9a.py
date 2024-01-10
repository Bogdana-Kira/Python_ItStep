from lxml import html
test = '''
    <html>
        <body>
            <div class="first_level">
                <h2 align='center'>one</h2>
                <h2 align='left'>two</h2>
            </div>
                <h2>another tag</h2>
        </body>
    </html>
'''
tree = html.fromstring(test)
tree.xpath('//h2')  # всі h2 теги
tree.xpath('//h2[@align]')  # h2 теги з атрибутом align
tree.xpath('//h2[@align="center"]') # h2 теги з атрибутом align рівним "center"
div_node = tree.xpath('//div')[0]  # div тег
div_node.xpath('.//h2')  # всі h2 теги, які є дочірніми div
