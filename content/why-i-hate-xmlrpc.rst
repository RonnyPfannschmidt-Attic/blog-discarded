why i hate xmlrpc
=================

:date: 2008-02-28
:tags: python, web, xml


lets assume the data is:
<sourcecode syntax="pycon">
>>> fun = [{"age": 20, "name": "hans", "titles": ["Dr", "Dipl"]},
...        {"age": 19, "name": "peter"}]
</sourcecode>
and you want to do
<sourcecode syntax="pycon">
>>> myrpc.people.add(fun)
</sourcecode>

the json data looks like this:
<sourcecode syntax="javascript">
{"method": 'people.add',
 "id": 1234,
  params:[
   [{"age": 20, "name": "hans", "titles": ["Dr", "Dipl"]}, 
    {"age": 19, "name": "peter"}]
  ]}
</sourcecode>
and the xmlrpc data looks like this
<sourcecode syntax="xml">
<methodcall>
<methodName>people.add</methodName>
<params>
 <param>
  <value><array><data>
   <value><struct>
    <member>
     <name>age</name>
     <value><int>20</int></value>
    </member>
    <member>
     <name>titles</name>
     <value><array><data>
      <value><string>Dr</string></value>
      <value><string>Dipl</string></value>
     </data></array></value>
    </member>
    <member>
     <name>name</name>
     <value><string>hans</string></value>
    </member>
   </struct></value>
   <value><struct>
    <member>
     <name>age</name>
     <value><int>19</int></value>
    </member>
    <member>
     <name>name</name>
     <value><string>peter</string></value>
    </member>
   </struct></value>
  </data></array></value>
 </param>
</params>
</sourcecode>

why doesn't xmlrpc look like this:

<sourcecode syntax="xml">
<methodCall xmlns=... name="people.add">
 <array>
  <struct>
    <value name="age" xsi:type="integer">20</value>
    <value name="name" xsi:type="string">hans</value>
    <array name="titles">
      <value xsi:type="string">Dr</value>
      <value xsi:type="string">Dipl</value>
    </array>
  </struct>
  <struct>
    <value name="age" xsi:type="integer">20</value>
    <value name="name" xsi:type="string">hans</value>
  </struct>
 </array>
</methodCall>
</sourcecode>

