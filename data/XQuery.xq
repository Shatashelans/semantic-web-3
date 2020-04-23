xquery version "3.1";

declare namespace ext="http://www.altova.com/xslt-extensions";

declare variable $count_elements as xs:integer := count(//items_list/phone);

declare variable $tag_of_complicated_element as xs:string := string(//items_list/phone[1]/company_name);

declare function local:n_tag_of_the_complicated_element($n as xs:integer?)
as xs:string?
{
	string(doc('updated.xml')//items_list/phone[1]/descendant::*[$n])
};

declare variable $ceil as xs:decimal := xs:decimal(150);

declare variable $floor as xs:decimal := xs:decimal(100);

declare variable $name as xs:string := xs:string('Apple');

<html>
  <head>
    <title>Semantic Web, Lab3, Oleksii Shatalov</title>
  </head>
  <body>
	<h1>Semantic Web, Lab 3, Oleksii Shatalov. Clean XQuery</h1>
    <h2>
      General amount of elements: {$count_elements}
    </h2>
    <h2>
      Info about complicated elements by attribute: id
    </h2>
    <ul> {
      for $i in //items_list/phone
      return
        <li>
          {data($i/@id)}
        </li>
    } </ul>
    <h2>
      Info about the 1st complicated element by tag: company
    </h2>
    <h2>
      {$tag_of_complicated_element}
    </h2>
    <h2>
      Number of element where name consists of more than 2 words:
    </h2>
    <ul> {
      for $i at $count in //items_list/phone
      where contains($i/model_name, ' ')
	  return
        <li>
          {$count}
        </li>
    } </ul>
    <h2>
      First tag in the complicated element: {local:n_tag_of_the_complicated_element(1)}
    </h2>
    <h2>
      Second tag in the complicated element: {local:n_tag_of_the_complicated_element(2)}
    </h2>
    <h2>
      Third tag in the complicated element: {local:n_tag_of_the_complicated_element(3)}
    </h2>
    <h2>
      Price and name filtering:
    </h2>
    <ul> {
      for $i at $count in //items_list/phone/price
      where xs:decimal($i) <= $ceil and xs:decimal($i) >= $floor and contains($i/../model_name, $name)
	  return
        <li>
          {$count}. {$i/../model_name}
        </li>
    } </ul>
    <h2>
      Every fifth element:
    </h2>
    <ul> {
      for $i at $count in //items_list/phone
      where $count mod 5 = 0
	  return
        <li>
          <p>{$count}. {$i/model_name}</p>
          <p>{$i/rating}</p>
        </li>
    } </ul>
    <h2>
      Every second element with amount of customers:
    </h2>
    <ul> {
      for $i at $count in //items_list/phone
      where $count mod 2 = 0
	  return
        <li>
          {$count}. {$i/amount_of_customers}
        </li>
    } </ul>
  </body>
</html>