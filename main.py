from lxml import etree


def parse_xml(path):
    with open(path, 'r') as file:
        xml_text = file.read()
    return etree.XML(xml_text)


def count_elements(root):
    count_elements_query = etree.XPath('count(//items_list/phone)')
    return int(count_elements_query(root))


def attributes_info(root):
    attributes_info_query = etree.XPath('//items_list/phone/@id')
    return attributes_info_query(root)


def first_element_attribute_info(root):
    first_element_attribute_info_query = etree.XPath('//items_list/phone[1]/company_name/text()')
    return first_element_attribute_info_query(root)[0]


def contain_several_words(root):
    contain_several_words_query = etree.XPath(
        "count(//items_list/phone/model_name[contains(text(),' ')]/../preceding-sibling::*) + 1")
    return int(contain_several_words_query(root))


def n_parameter_of_complicated_element(root, number):
    n_parameter_of_complicated_element_query = etree.XPath('(//items_list/phone[1]/descendant::*)[$number]/text()')
    return n_parameter_of_complicated_element_query(root, number=number)[0]


def tag_name_with_name_and_range(root, ceil, floor, name):
    tag_name_with_name_and_range_query = etree.XPath(
        '//items_list/phone/price[number(text()) <= $ceil and number(text()) >= $floor]/../model_name[contains(text(), '
        '$name)]/text()')
    return tag_name_with_name_and_range_query(root, ceil=ceil, floor=floor, name=name)


def every_fifth_element(root):
    element_number_query = etree.XPath('//items_list/phone[position() mod 5 = 0]/@id')
    element_number = list(map(lambda x: int(x.replace('result_', '')) + 1, element_number_query(root)))
    element_info_each_fifth_query = etree.XPath('//items_list/phone[position() mod 5 = 0]/model_name/text()')
    element_info_each_fifth = element_info_each_fifth_query(root)
    element_rating_query = etree.XPath('//items_list/phone[position() mod 5 = 0]/rating/text()')
    element_rating = list(map(lambda x: float(x), element_rating_query(root)))
    return element_number, element_info_each_fifth, element_rating


def every_second_element(root):
    element_number_query = etree.XPath('//items_list/phone[position() mod 2 = 0]/@id')
    element_number = list(map(lambda x: int(x.replace('result_', '')) + 1, element_number_query(root)))
    element_amount_of_customers_query = etree.XPath('//items_list/phone[position() mod 2 = 0]/amount_of_customers/text()')
    element_amount_of_customers = element_amount_of_customers_query(root)
    return element_number, element_amount_of_customers


if __name__ == '__main__':
    root = parse_xml('data/updated.xml')
    print('General amount of elements: ' + str(count_elements(root)))
    print('\r\nInfo about complicated elements by attribute: id')
    # map(lambda x: print(x + '; '), list(attributes_info(root)))
    print(attributes_info(root))
    print('\r\nInfo about the 1st complicated element by tag: company')
    print(first_element_attribute_info(root))
    print('\r\nNumber of one element where name consists of more than 2 words: ' + str(contain_several_words(root)))
    print('\r\nFirst tag in the complicated element: ' + n_parameter_of_complicated_element(root, 1))
    print('\r\nSecond tag in the complicated element: ' + n_parameter_of_complicated_element(root, 2))
    print('\r\nThird tag in the complicated element: ' + n_parameter_of_complicated_element(root, 3))
    print('\r\nPrice and name filtering:')
    print(tag_name_with_name_and_range(root, ceil=150, floor=100, name='Apple'))
    print('\r\nEvery fifth element:')
    element_number, element_info_each_fifth, element_rating = every_fifth_element(root)
    for i in range(len(element_number)):
        print(str(element_number[i]) + '. ' + element_info_each_fifth[i] + '  RATING: ' + str(element_rating[i]))
    print('\r\nEvery second element with amount of customers:')
    element_number, element_amount_of_customers = every_second_element(root)
    for i in range(len(element_number)):
        print(str(element_number[i]) + '. ' + element_amount_of_customers[i])
