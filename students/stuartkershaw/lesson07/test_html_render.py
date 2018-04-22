from io import StringIO
from html_render import Element


def test_type_Element():
    test_element = Element(content=None)
    assert isinstance(test_element, Element) is True


def test_class_attributes_Element():
    test_element = Element(content=None)
    assert test_element.tag_name == 'html'
    assert test_element.indentation == 2


def test_instance_attributes_Element():
    test_element = Element(content=None)
    assert test_element.content == []


def test_append_content_Element():
    test_element = Element(content=None)
    test_element.append('New content')
    assert test_element.content == ['New content']


def test_render_page_Element():
    test_element = Element(content="Some content.")
    test_element.append('Some more content.')

    f = StringIO()
    test_element.render(f, "    ")

    assert f.getvalue() == '<html>\nSome content. Some more content.\n</html>'
