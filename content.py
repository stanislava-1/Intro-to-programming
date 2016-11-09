# This file contains all the page content. I put the content into this separate
# file so that I could use one template (lesson.html) for every lesson.

# It is divided into strings stored in variables and get rid of most of html tags,
# which are contained in the template lesson.html now. 

# Here is the key for understanding the names of the variables:

# title of a lessons - S4L1, S4L2 ... (e. g. S4L1 means Stage 4 Lesson 1)

# titles of lesson parts - title_411, title_412 ... (the firs number is the Stage  
#                          number, the second number is the Lesson number, the third 
#                          number is the Part number)

# contents of lesson parts - part_411, part_412 ... (the meaning of numbering
#                            is the same as in case of part titles)

# -------------------------- Content Strings --------------------------------------

# Stage 1

stage_1 = 'Stage 1'
title_1 = 'Make a Webpage'
description_1 = """\
The goal of Stage 1 is to <b>make a webpage</b> using the basic knowledge of \
Internet, HTML, CSS and how they work together. The basic knowledge is \
delivered mainly trough the first lessons of these Udacity courses: <a href=\
"https://www.udacity.com/course/intro-to-html-and-css--ud304">Intro to HTML \
and CSS</a> and <a href="https://www.udacity.com/course/web-development--cs253">\
Web Development</a>.\
"""

# Stage 1, Lesson 1:

S1L1 = '1. The Basics of the Web and HTML'

title_111 = 'World Wide Web'
part_111 = """
The main type of document on the web is <strong>HTML</strong>. In other \
words, World Wide Web is a collection of HTML documents. But there can be \
also other types of files there, such as: plain text, pdf, images etc.

To make the web work, there have to be:

<ul>\
<li>person who wants to see the web</li>\
<li>computer + browser</li>\
<li>internet</li><li>servers</li>\
<li>HTML</li>\
</ul>	

Look at <a href="https://www.udacity.com/course/viewer#!/c-nd000/l-3873828673/\
e-48329854/m-48480496">this video</a> to understand communication between \
the things listed above.
"""

title_112 = 'Tags and Elements'
part_112 = """
In HTML we use <strong>tags</strong> (opening an closing tags) and \
<strong>elements</strong>. <strong>Element</strong> is the whole "thing" \
consisting of <strong>opening tag</strong>, <strong>closing tag</strong> and \
the <strong>content</strong> between these tags. Content is that part of the \
element that is visible also on the webpage.

Look at related <a href="https://www.udacity.com/course/viewer#!/c-nd000/\
l-3873828673/m-48723444">video</a>.
"""

title_113 = 'Do not forget computers are "stupid"'
part_113 = """
When you communicate with computer, you must give it <b>absolutely exact \
information</b>. Computer is not a person and it is not able to "read between \
the lines" or to understand you when you make a mistake.

<i><b>Example:</b> If you are a woman, you know, that if a man says he wants \
a "red" pencil and you do not see any red pencil, he probably means, he wants \
the "dark-orange" or the "dark-pink" pencil (you are able to know it because \
you are more clever then computer). But if the same man tells computer "red", \
computer understands "red". This could produce an error or not desired result \
:-).</i>
"""

title_114 = 'Inline and Block elements'
part_114 = """
The main difference between inline elements and block elements is that \
<strong>the block elements create a box around the content</strong> of the \
element. The box is invisible, but it has its <b>width</b> and <b>hight</b>. \
Inline elements do not do that.
"""

#Stage 1, Lesson 2:

S1L2 = '2. Creating a structured document'

title_121 = 'How to see the structure of any web'
part_121 = """
Here are the steps:

<ol>\
<li>Open a web page (e. g. wikipedia)</li><li>Find a three lined button in \
the top right corner of the window (Customize and control Google Chrome) and \
click it</li>\
<li>Find Tools (of More tools) in the list</li>\
<li>Click <strong>Developer tools</strong></li>\
</ol>

Now you can see the structure of the page in <em>Elements</em>. The structure \
is created with HTML.

You can change anything in the <em>Elements</em> or <em>Styles</em> and \
observe how the page changes. To return the former look of the page just \
refresh the page.
"""

title_122 = 'Tree-like Structure'
part_122 = """
The structure of a webpage is a tree-like structure. Programmers call it \
<strong>DOM</strong> (Document Object Model). Look at \
<a href="https://en.wikipedia.org/wiki/Tree_(data_structure)">this page</a> \
for explanation.
"""

title_123 = 'Boxes, boxes ... and boxes'
part_123 = """
Web consists of boxes. Everything on a web is a box, even if it does not look \
like a box. In HTML boxes are structured in elements. Every box is stored in \
its own element (div tags).
"""

title_124 = 'Editor for programmers'
part_124 = """
For writing codes, we need an <b>appropriate editor</b> and know how to work \
with it. For bigger projects <strong>Sublime Text</strong> is recommended. \
<a href="https://www.udacity.com/course/viewer#!/c-nd000/l-4142419359/\
m-3752118868">Here</a> is information about text editors, how to work with \
them and when to use them.
"""

#Stage 1, Lesson 3:

S1L3 = '3. Adding CSS style and HTML structure'

title_131 = 'HTML and CSS - what they do'
part_131 = """
Both are languages, but they have different roles:

<ul>\
<li>HTML (Hypertext Markup Language) makes the <strong>"structure"</strong> \
of a web page.</li>\
<li>CSS (Cascading Style Sheets) makes the <strong>"style"</strong> of a page \
(how it looks).</li>\
</ul>

To give a CSS style to a HTML file, we can:

<ul>\
<li>make an <b>extra CSS file</b> which "cooperates" with the HTML file or</li>\
<li>use <b>style tags</b> and write the CSS code to the head of the HTML file \
(a method for smaller projects).</li>\
</ul>

<a href="https://www.udacity.com/course/viewer#!/c-nd000/l-4131369051/\
e-3614428682/m-2603798584">Here</a> is the example of applying CSS style on \
a HTML document using the first method.


Of course, we can define styles also directly in the body-elements of HTML \
(<i>inline style</i>), but this is really a very bad idea for bigger projects.
"""

title_132 = 'Avoiding repetition'
part_132 = """
One of the main reasons why using inline style in HTML is a bad idea is that \
while using this mathod we have to repeate the same code at many places in \
the HTML document. This can be avoided by using an extra CSS file for \
defining styles. The great thing about this is that it <strong>allows us to \
define an uniform style for more elements at one time</strong>, so we do not \
have to arduously repeat the style code for every element separately. \
It saves time, reduces making copy-paste errors, allows to write/change \
codes more efficiently.
"""

title_133 = 'Inheritance in CSS'
part_133 = """
Inheritance in CSS means that the rules defined for an element are not \
applied only for the matching element, but <b>also for its "childs"</b> \
- elements inside the element (if "childs" do not have their own rules \
defined). \
<a href="https://en.wikipedia.org/wiki/Cascading_Style_Sheets#Inheritance">\
Here</a> is the explanation and example.
"""

title_134 = 'CSS selectors'
part_134 = """
There are several ways how to <b>select a HTML element</b> for which we want \
to define a certain CSS style. For example, we can decide to define a style \
for all h1 elements. Or we can decide to determine a style for every element \
with class="description". The <strong>CSS selector</strong> is the "thing" \
by which we find all HTML elements for which the rule is defined. Read \
<a href="https://css-tricks.com/how-css-selectors-work/">this article</a> \
for better explanation on selectors.
"""

title_135 = 'Writing code in CSS'
part_135 = """
When we write code in CSS, first goes the <b>selector</b> and then \
<b>curly brackets</b> with <b>the rule inside</b>. Find examples \
<a href="https://www.udacity.com/course/viewer#!/c-nd000/l-4131369051/\
m-3611108698">here</a>.
"""

title_136 = 'Other'
part_136 = """
There are really many things we can study about HTML and CSS. The best way \
how to learn them is to read articles, watch videos, read codes that someone \
else wrote and the most important - to <b>test</b> it. For example on \
a simple trial project such as this one.
"""

# ------------------------------------------------------------------------------------

# Stage 2:

stage_2 = 'Stage 2'
title_2 = 'Build a Mad Libs Game'
description_2 = """\
Stage 2 is focused on <strong>Python basics</strong> - syntax, variables, \
strings, functions, if statements, loops and debugging. The lessons of this \
stage drow from the course <a href="https://www.udacity.com/course/intro-to-\
computer-science--cs101">Intro to Computer Science</a>. The goal of this \
stage final project is to build a <b>Mad Libs Game</b> which is not included \
in this webpage.
"""

# Stage 2, Lesson 1:

S2L1 = '1. Introduction to serious programming'

title_211 = 'Programming'
part_211 = """
Firstly, let's clarify several terms related to programming:

<ul>\
<li>A <strong>computer</strong> is a machine that can execute a program. With \
the right program, a computer can do any mechanical computation you can \
imagine.</li>\
<li>A <strong>program</strong> describes a very precise sequence of steps. \
Since the computer is just a machine, the program must give the steps in \
a way that can be executed mechanically. That is, the program can be followed \
without any thought.</li>\
<li>A <strong>programming language</strong> is a language designed for \
producing computer programs. A good programming language makes it easy for \
humans to read and write programs that can be executed by a computer.</li>\
<li><strong>Python</strong> is a programming language. The programs that we \
write in the Python language will be the input to the <strong>Python \
interpreter</strong>, which is a program that runs on the computer. The Python \
interpreter reads our programs and executes them by following the rules of the \
Python language.</li>\
</ul>
"""

title_212 = 'Why programming languages are needed?'
part_212 = """
We need them because <b>natural languages</b> (like English) <b>are not \
suitable for programming</b>. Natural languages are:

<ol>\
<li><i>Ambiguous</i>. To program computers, <b>it is important that we \
(and computers) know exactly what our programs mean</b>.</li>\
<li>Very <i>verbose</i>. Programming languages are brief because <b>we want \
our programs to be short</b> so it does not take a lot of time to write them, \
read them and understand them.</li>\
</ol>
"""

title_213 = 'Grammar of programming languages'
part_213 = """
Programming languages (like Python) have a <b>strict grammatical structure</b> \
and we have to use it always correctly. If not, the result will be an error or \
a not desirable result. 
"""

title_214 = 'Python expressions'
part_214 = """
In Python expression means <b>something that has a value</b>. There are more \
posibilities how the value could look like in Python, but we will learn about \
it later. For now, here are some examples of arithmetic expresions:

<ul class="no-bullets">\
<li class="more-space"><span class="code-frame">5</span></li>\
<li class="more-space"><span class="code-frame">5 - 5</span></li>\
<li class="more-space"><span class="code-frame">2.0 * (6 + 8)/3</span></li>\
</ul>
"""

title_215 = 'Print'
part_215 = """
To see what our code does when we run it, we use the command <span class=\
"code-frame">print</span>. For example, when we ad this command before the \
above mentioned expressions and run the program, we get these results:

<ul class="no-bullets">\
<li class="more-space">code: <span class="code-frame">print 5</span> result: \
<span class="code-frame">5</span></li>\
<li class="more-space">code: <span class="code-frame">print 5 - 5</span> \
result: <span class="code-frame">0</span></li>\
<li class="more-space">code: <span class="code-frame">print 2.0 * (6 + 8)/3\
</span> result: <span class="code-frame">9.33333333333</span></li>\
</ul>
"""

title_216 = 'Indentation'
part_216 = """
Indentation is very important in Python. It causes error if we don't use it \
when it is needed or vice versa if we use it when it is not required. 
"""

#Stage2, Lesson 2:

S2L2 = '2. Variables and Strings'

title_221 = 'Variables'
part_221 = """
A <strong>variable</strong> is a <em>name</em> that refers to a <em>value</em>.

<h3 class="gama">Name of a variable</h3>

For the name of a variable we can use any group of letters and numbers and \
underscores (_) <b>but it must not start with a number</b>, e. g:

Valid names:

<ul class="no-bullets">\
<li class="more-space"><span class="code-frame">age</span></li>\
<li class="more-space"><span class="code-frame">speed_of_light</span></li>\
<li class="more-space"><span class="code-frame">text123</span></li>\
</ul>

Invalid name:

<ul class="no-bullets">\
<li class="more-space"><span class="code-frame">2015tuition</span></li>\
</ul>

For names, we can use both-lower case and upper-case letters, but it is \
recommended to use only lower-case letters (to avoide mistakes).

<h3 class="gama">Value of a variable</h3>

A variable has a value we <strong>assign</strong> to it and we do it this way:

<span class="code-frame">variable = expression</span>, e.g.: <span class=\
"code-frame">number = 1</span>

<h3 class="gama">Meaning of <span class="code-frame">=</span></h3>

It is important to realize that <span class="code-frame">=</span> in Python \
has different meaning than <span class="code-frame">=</span> in mathematics:

<b>In mathematics</b> the statement <span class="code-frame">5 + 3 = 8</span> \
means that <span class="code-frame">5 + 3</span> is the same as <span class=\
"code-frame">8</span>.

<i>On the other hand:</i>

<b>In Python</b> the statement <span class="code-frame">number = 1</span> \
means that the variable <span class="code-frame">number</span> is assigned \
the value <span class="code-frame">1</span>.

<h3 class="gama">Variables can vary</h3>

The value of a variable does not have to be the same forever. We can change \
it. In a certain time a variable refers to the value it was assigned last.

If we run a code like this:

<table class="code-frame">\
<tr>\
<td>age = 50</td>\
</tr>\
<tr>\
<td>age = age + 1</td>\
</tr>\
<tr>\
<td>print age</td>\
</tr>\
</table>

the resul will be: <span class="code-frame">51</span>.
"""

title_222 = 'Strings'
part_222 = """
A string is a <b>sequence of characters surrounded by quotes</b> (either \
single or double):

<ul class="no-bullets">\
<li class="more-space"><span class="code-frame">'a string with single quotes'\
</span></li>\
<li class="more-space"><span class="code-frame">"a string with double quotes"\
</span></li>\
</ul>

A string can be for example a sentence <span class="code-frame">'Hallo \
everybody!'</span>, a word <span class="code-frame">'Hallo'</span>, a part of \
word <span class="code-frame">'allo'</span>, a character <span class="code-\
frame">'a'</span>or empty string <span class="code-frame">''</span>, etc.

If you run this code:

<span class="code-frame">print 'Python'</span>

the result is:

<span class="code-frame">Python</span>

But <b>if you forget the quotes</b>, Python will think it is a variable name. \
And since it is not assigned any value, it will produce an error.

As for <b>numbers</b>, a number in quotes is not treated like a number, but \
like a string, too.

<h3 class="gama">Using operators on strings</h3>

We can use <strong>plus operator</strong> on strings, but its meaning is \
different form its meaning while using it with integers. Look at the 
difference:

<ul class="no-bullets">\
<li class="more-space">code: <span class="code-frame">print 5 + 3</span> \
result: <span class="code-frame">8</span></li>\
<li class="more-space">code: <span class="code-frame">print '5' + '3'</span> \
result: <span class="code-frame">53</span></li>\
</ul>

We can aslo <strong>multiply strings</strong>:

<span class="code-frame">print 'GO! ' * 3</span> produces: <span class=\
"code-frame">GO! GO! GO! </span>

<h3 class="gama">Indexing strings</h3>

Indexing strings is <b>selecting sub-sequences from strings</b> and we do it \
this way:

<div class = "tables">\
<div class="one-table">\
<table class="code-frame">\
<tr>\
<td>string = 'Stanislava'</td>\
</tr>\
<tr>\
<td>print string[0]</td>\
</tr>\
</table>\
<p>\
result: <span class="code-frame">S</span>\
</p>\
</div>\
<div class="one-table">\
<table class="code-frame">\
<tr>\
<td>string = 'Stanislava'</td>\
</tr>\
<tr>\
<td>print string[1]</td>\
</tr>\
</table>\
<p>\
result: <span class="code-frame">t</span>\
</p>\
</div>\
<div class="one-table">\
<table class="code-frame">\
<tr>\
<td>string = 'Stanislava'</td>\
</tr>\
<tr>\
<td>print string[7]</td>\
</tr>\
</table>\
<p>\
result: <span class="code-frame">a</span>\
</p>\
</div>\
</div>\

The numbering of positions in a string <b>starts from 0</b>.

If we use <b>negative numbers</b> in the index it starts counting from the \
back of the string:

<div class = "tables">\
<div class="one-table">\
<table class="code-frame">\
<tr>\
<td>string = 'Stanislava'</td>\
</tr>\
<tr>\
<td>print string[-1]</td>\
</tr>\
</table>\
<p>\
result: <span class="code-frame">a</span>\
</p>\
</div>\
<div class="one-table">\
<table class="code-frame">\
<tr>\
<td>string = 'Stanislava'</td>\
</tr>\
<tr>\
<td>print string[-2]</td>\
</tr>\
</table>\
<p>\
result: <span class="code-frame">v</span>\
</p>\
</div>\
<div class="one-table">\
<table class="code-frame">\
<tr>\
<td>string = 'Stanislava'</td>\
</tr>\
<tr>\
<td>print string[-6]</td>\
</tr>\
</table>\
<p>\
result: <span class="code-frame">i</span>\
</p>\
</div>\
</div>\

<b>When you try to index a character in a position where there is none</b>, \
Python produces an error.

<h3 class="gama">Selecting longer sub-sequences</h3>

If we want the sub-sequence to be <b>more then one character</b>, we have to \
designate an <b>interval</b> - the starting point and the ending point of the \
sub-sequence. The result is a sub-sequence that starts from the starting point \
and <b>ends on the position one step before the ending point</b>. Examples:

<div class = "tables">\
<div class="one-table">\
<table class="code-frame">\
<tr>\
<td>string = 'Slovakia'</td>\
</tr>\
<tr>\
<td>print string[0:4]</td>\
</tr>\
</table>\
<p>\
result: <span class="code-frame">Slov</span>\
</p>\
</div>\
<div class="one-table">\
<table class="code-frame">\
<tr>\
<td>string = 'Slovakia'</td>\
</tr>\
<tr>\
<td>print string[2:3]</td>\
</tr>\
</table>\
<p>\
result: <span class="code-frame">o</span>\
</p>\
</div>\
<div class="one-table">\
<table class="code-frame">\
<tr>\
<td>string = 'Slovakia'</td>\
</tr>\
<tr>\
<td>print string[4:8]</td>\
</tr>\
</table>\
<p>\
result: <span class="code-frame">akia</span>\
</p>\
</div>\
</div>\

In case we don't give any number as a starting point or as an ending point \
(or both), it behaves like this:

<div class = "tables">\
<div class="one-table">\
<table class="code-frame">\
<tr>\
<td>string = 'Slovakia'</td>\
</tr>\
<tr>\
<td>print string[:5]</td>\
</tr>\
</table>\
<p>\
result: <span class="code-frame">Slovak</span>\
</p>\
</div>\
<div class="one-table">\
<table class="code-frame">\
<tr>\
<td>string = 'Slovakia'</td>\
</tr>\
<tr>\
<td>print string[3:]</td>\
</tr>\
</table>\
<p>\
result: <span class="code-frame">vakia</span>\
</p>\
</div>\
<div class="one-table">\
<table class="code-frame">\
<tr>\
<td>string = 'Slovakia'</td>\
</tr>\
<tr>\
<td>print string[:]</td>\
</tr>\
</table>\
<p>\
result: <span class="code-frame">Slovakia</span>\
</p>\
</div>\
</div>\

<h3 class="gama">Find</h3>

The function <em>find</em> is the oposite of indexing. Using this function \
we <b>find the position of a sub-sequence</b> in a string:

<table class="code-frame">\
<tr>\
<td>string = 'Stanislava'</td>\
</tr>\
<tr>\
<td>print string.find('slava')</td>\
</tr>\
</table>\

result: <span class="code-frame">5</span>

This means that the first occurance of sub-sequence 'slava' in the string \
starts on the position 5.

If we want to look for the sub-sequence <b>from other position then 0</b>, \
we do it this way:

<table class="code-frame">\
<tr>\
<td>string = 'Stanislava Stanislava'</td>\
</tr>\
<tr>\
<td>print string.find('slava', 6)</td>\
</tr>\
</table>\

result: <span class="code-frame">16</span>

This means that the firs occurance of 'slava' in the string from position 6 \
starts on the position 16.

In case we try to find something that <b>the string does not contain</b>, \
Python returns <span class="code-frame">-1</span>.
"""

#Stage2, Lesson 3:

S2L3 = '3. Input -> Function -> Output'

title_231 = 'What is a function/procedure'
part_231 = """
There are many functions in Python defined already. Also <em>find</em> is \
a function. But we can define our own functions if we need (and we need it \
often).

A function is <b>a piece of code which takes an input and produces an \
output</b>. It is valid for different values of the input and it depends on \
the value of the input what will be the value ot the output.
"""

title_232 = 'The structure of a function'
part_232 = """
The usual structure of a function is following:

<table class="code-frame">\
<tr>\
<td><pre><i>def</i> &lt;name&gt;(&lt;input/inputs&gt;):<br>\
    &lt;body&gt;<br>\
    return &lt;output/outputs&gt;</pre></td>\
</tr>\
</table>

It must begin with <b><i>def</i></b> which is an abbreviation of "definition".

The <b>name</b> is the name of the function. The <b>input</b> or inputs are \
the parameters we need for this function. They are in parenthesis and there \
must be a colon after that. The <b>body</b> is the code of the function. The \
<b>return</b> determines the output of the function. In fact, it is a part of \
a <b>body</b>, but I separated it because of its high importance. The \
<b>output</b> (or outputs) is the result we want to achieve by using the 
function. There can be more then one input in a function and it can produce \
more then one output.
"""

title_233 = 'Making and using functions'
part_233 = """
An example of a simple function (<em>how to make it</em>):

<table class="code-frame">\
<tr>\
<td><pre><i>def</i> usd(number):<br>\
    price = str(number) + ' USD'<br>\
    return price</pre></td>\
</tr>\
</table>

And here is how it works (<em>how to use it</em>):

<table class="code-frame">\
<tr>\
<td>number = 100</td>\
</tr>\
<tr>\
<td>print usd(number)</td>\
</tr>\
</table>\

result: <span class="code-frame">100 USD</span>
"""

title_234 = 'Return vs. print vs. nothing'
part_234 = """
To get the output from a function we have to use <b>return</b>. In some cases \
we can use <b>print</b> instead, but usually <b>return</b> is more useful. \
<strong>!!! Without return (or print) the function always produces <i>None</i> \
!!!</strong>
"""

title_235 = 'Why to make functions'
part_235 = """
The advantage of a function is that we make it only once but then we can use \
it for diferent values of inputs. In other words, <strong>they help us to \
avoid repetition</strong> in writing codes.
"""

#Stage2, Lesson 4:

S2L4 = '4. Control Flow &amp; Loops: If and While'

title_241 = 'Making decisions'
part_241 = """
If we want our code to behave diferently in various cases, firstly we need to \
understand how Python makes decisions about statements.

<strong>Python is able to evaluate whether a statement is true or not</strong> \
an accordingly it brings value <em>True</em> or value <em>False</em>, e. g:

<ul class="no-bullets">\
<li class="more-space">code: <span class="code-frame">print 5 &gt; 3</span> \
result: <span class="code-frame">True</span></li>\
<li class="more-space">code: <span class="code-frame">print 10 &lt; 2</span> \
result: <span class="code-frame">False</span></li>\
<li class="more-space">code: <span class="code-frame">print 2*4 != 8</span> \
result: <span class="code-frame">False</span></li>\
<li class="more-space">code: <span class="code-frame">print 2*4 == 8</span> \
result: <span class="code-frame">True</span></li>\
</ul>

<span class="code-frame">!=</span> means "is not equal to". <span class=\
"code-frame">==</span> means "is equal to". 
"""

title_242 = 'If Statements'
part_242 = """
The structure of <em>If Statement</em> is following:

<table class="code-frame">\
<tr>\
<td><pre>If &lt;testExpression&gt;:<br>\
    &lt;block&gt;</pre></td>\
</tr>\
</table>\

The code in the <b>block</b> runs only if the <b>testExpresion</b> is \
<i>True</i>.
"""

title_243 = 'How to use If Statements'
part_243 = """
In the following example we use an <i>If Statement</i> in a function that \
creates a greeting in the form 'Hallo Name' in case the input (name) is not \
an empty string:

<table class="code-frame">\
<tr>\
<td><pre>def greeting(name):<br>\
    if name != '':<br>\
    	return 'Hallo ' + name + '!'</pre></td>\
</tr>\
</table>\

<div class = "tables">\
<div class="one-table">\
<p>If <i>name</i> <b>is not</b> an empty string - <b>the statement is \
<i>True</i></b>, the code under <i>if</i> <b>runs</b> and returns a result:</p>\
<table class="code-frame">\
<tr>\
<td>print greeting('Jane')</td>\
</tr>\
</table>\
<p>\
result: <span class="code-frame">Hallo Jane!</span>\
</p>\
</div>\
<div class="one-table">\
<p>If <i>name</i> <b>is</b> an empty string - <b>the statement is \
<i>False</i></b>, the code under <i>if</i> <b>does not</b> run and the \
function returns <i>None</i>:</p>\
<table class="code-frame">\
<tr>\
<td>print greeting('')</td>\
</tr>\
</table>\
<p>\
result: <span class="code-frame">None</span>\
</p>\
</div>\
</div>\
"""

title_244 = 'Else Expressions'
part_244 = """
But maybe we do not like that our code returns <i>None</i> in some cases. \
Luckily, we can write <b>an alternative code</b> for the cases when the \
<em>If statement</em> is not <i>True</i>. There are two ways how to do it.

The first one is using <b><em>else</em></b>:

<table class="code-frame">\
<tr>\
<td><pre>def greeting(name):<br>\
    if name != '':<br>\
    	return 'Hallo ' + name + '!'<br>\
    else:<br>\
    	return 'What is your name?'</pre></td>\
</tr>\
</table>\

Then the result of <span class="code-frame">print greeting('')</span> will \
not be <i>None</i>, but: <span class="code-frame">What is your name?</span>.

But we can write the code also this way:

<table class="code-frame">\
<tr>\
<td><pre>def greeting(name):<br>\
    if name != '':<br>\
    	return 'Hallo ' + name + '!'<br>\
    return 'What is your name?'</pre></td>\
</tr>\
</table>\

It will do exactly the same job as the code with <i>else</i> and it is \
shorter, but <b>the code with <em>else</em> is more transparent</b>.
"""

title_245 = 'While Loops'
part_245 = """
The structure of a <em>While Loop</em>:

<table class="code-frame">\
<tr>\
<td><pre>While &lt;testExpression&gt;:<br>\
    &lt;block&gt;</pre></td>\
</tr>\
</table>

It is the same as the structure of the <i>If statement</i> but it doesn't \
do the same job. <i>If statement</i> runs the code only once (if the \
testExpression is <i>True</i>) or it does not run it at all (if the \
testExpression is <i>False</i>), but <strong><i>while loop</i> runs the \
code over and over as long as the testExpression is <i>True</i></strong> \
(0, 1, 2, 3 ... or more times).
"""

title_246 = 'How to use While Loops'
part_246 = """
In the following code is used a <i>while loop</i>. The function takes a \
positive number as input and returns all numbers starting from 1 and ending \
with the input number.

<div class="tables">\
<div class="one-table">\
<table class="code-frame">\
<tr>\
<td><pre>def print_numbers(x):<br>\
    i = 1<br>\
    while i &lt;= x:<br>\
    	print i<br>\
    	i = i + 1</pre></td>\
</tr>\
</table>\
</div>\
<div class="one-table">\
<table class="code-frame">\
<tr>\
<td>print print_numbers(3)</td>\
</tr>\
</table>\
</div>\
<div class="one-table">\
<table>\
<tr>\
<td>-&gt; result:</td>\
</tr>\
</table>\
</div>\
<div class="one-table">\
<table class="code-frame">\
<tr>\
<td>1</td>\
</tr>\
<tr>\
<td>2</td>\
</tr>\
<tr>\
<td>3</td>\
</tr>\
</table>\
</div>\
</div>\
"""

title_247 = 'Break'
part_247 = """
The problem with while loops is that if the textExpression never becomes \
<i>False</i>, the code never stops. It is not what we want. In such cases \
we use <span class="code-frame">break</span> which stops the code in a certain moment \
(usually when some if statement under while loop becomes True).
"""

#Stage2, Lesson 5:

S2L5 = '5. Debugging'

title_251 = 'Bugs and debugging'
part_251 = """
<strong>Bug</strong> is an unexpected defect, fault, flaw, or imperfection. \
Simply - a mistake. In programming bugs are common. A little mistake can \
cause big problems. But there is a way, how to look for bugs effectively. \
Seeking and removing bugs in codes is called <strong>debugging</strong>.
"""

title_252 = 'Debugging strategies'
part_252 = """
To find a bug, we should do following: 

<h3 class="gama">Examine error messages when programs crash</h3>

The last line of Python Tracebacks will tell you what went wrong. Reading \
backwards from there will tell you more about where the problem occurred.

<h3 class="gama">Work from example code</h3>

If your modified code doesn't work, comment it out and do step-by-step \
modifications to the example code until it does what you want.

<h3 class="gama">Make sure examples work</h3>

Just because you find example code doesn't mean it will work in your \
system. Check the example code you're using to make sure it behaves the \
way you expect.

<h3 class="gama">Check (print) intermediate results</h3>

When your code doesn't crash, but doesn't behave as expected, add print \
statements to your program to see where in the code things stop behaving \
correctly.

<h3 class="gama">Keep and compare old versions</h3>

When you have a working version of your code, save it before you add to \
the code. This will give you something to go back to if you introduce too \
many new bugs.
"""

# ------------------------------------------------------------------------------------

# Stage 3:

stage_3 = 'Stage 3'
title_3 = 'Create a Movie Website'
description_3 = """\
In Stage 3 we continue learning Python, but focus on <strong>Object Oriented \
Programming</strong>. We learn about the relations between classes, functions \
and objcets (instances) and as a final project create a <b>movie website</b>.\
"""

# Stage 3, Lesson 1:

S3L1 = 'Movie Website'

title_311 = 'Object Oriented Programming?'
part_311 = """
As making notes of this stage wasn't a part of stage final project, it was \
not required to add them to the webpage. Therefore, you won't find a lot of \
information here.

The goal of Stage 3 of IPND is to create a <b>Movie Website</b>. In fact, \
the website is created already, our task was only to fill in the page with \
our favourite movies and optionaly, to make some changes.

To make your own content of the movie website (and make some changes there), \
it is necessary to: \

<ul>\
<li>understand the basics of <strong>Object Oriented Programming</strong></li>\
<li>understand a code that was written by someone else than me</li>\
</ul>

Most of the Stage 3 content is drown from the Udacity course <a href="https:\
//www.udacity.com/course/programming-foundations-with-python--ud036"><strong>\
Programming Foundations with Python</strong><a>. 
"""

# ------------------------------------------------------------------------------------

# Stage 4:

stage_4 = 'Stage 4'
title_4 = 'Allow Comments'
description_4 = """\
This stage is about servers, making forms, templates and databases. Most of \
the lessons are taken from the course <a href="https://www.udacity.com/course/\
web-development--cs253">Web Development</a>. The task in the stage final \
project is to set the page to be online and to <b>allow adding comments by \
users</b>.\
"""

# Stage 4, Lesson 1:

S4L1 = '1. Introduction to networks'

title_411 = 'What is a network?'
part_411 = """
A <strong>network</strong> is a group of entities that can communicate, even \
though they are not directly connected. If they can communicate directly it \
is not a network.

The <strong>Internet</strong> is a particular type of network.
"""

title_412 = 'What is needed to make a network?'
part_412 = """
To make a network like internet, we need:

<ul>\
<li>a way to encode and interpret messages</li>\
<li>a way to route messages</li>\
<li>rules for deciding who gets to use resources</li>\
</ul>
"""

title_413 = 'Latency, bandwidth, bits'
part_413 = """
<strong>Latency</strong> is the time it takes a message to get from the source \
to the destination.

<strong>Bandwidth</strong> is the amount of information that can be transmitted \
per unit of time.

A <strong>bit</strong> is the smallest unit of information.
"""

# Stange 4, Lesson 2:

S4L2 = '2. Servers'

title_421 = 'Server'
part_421 = """
A <strong>server</strong> is both a running instance of some software that \
is capable of accepting requests from clients, and the computer that executes \
such software.

Here is a very simple scheme of how servers work:

<img src="static/images/servers.png" alt="servers scheme" class="img-lesson">   
"""

title_422 = 'URL-s'
part_422 = """
<strong>URL</strong> (A Uniform Resource Locator) is a reference to a web \
resource that specifies its location on a computer network and a mechanism \
for retrieving it. In common speech, URL is often meant as a <b>web \
address</b>, but it is not exactly the same thing. 

URL can look like this:

<span class="code-frame">http://www.udacity.com/cs253x/hipmunk.png</span>

Let's divide it to parts:

<ul>\
<li class="more-space"><span class="code-frame">http</span> is a protocol</li>\
<li class="more-space"><span class="code-frame">www.udacity.com</span> is a \
host</li>\
<li class="more-space"><span class="code-frame">/cs253x/hipmunk.png</span> is \
a path. Minimum path is <span class="code-frame">/</span>.</li>\
</ul>

<h3 class="gama">Parameters</h3>

If there is a <strong>parameter</strong> in url, the url may look like this:\

<span class="code-frame">http://www.example.com/foo<span class="red">?p=1\
</span></span>

In this case, <span class="code-frame">p</span> is a parameter name and \
<span class="code-frame">1</span> is a parameter value.

If there are more parameters in url, they are separated with <span \
class="code-frame">&amp;</span>:

<span class="code-frame">http://www.example.com/foo?p=1<span class="red">\
&amp;</span>q=2</span>

<h3 class="gama">Fragments</h3>

A <strong>fragment</strong> is a part of a page. A URL which refers to a part \
of a page looks like this:

<span class="code-frame">http://www.example.com/foo?p=1<span class="red">\
#fragment</span></span>

<span class="code-frame">fragment</span> is the name of the page part.

<h3 class="gama">Port</h3>

URL may look also like this:

<span class="code-frame">http://localhost:<span class="red">8000</span>/</span>

where localhost is the name ot the machine and the number is a <strong>port\
</strong>.
"""

title_423 = 'HTTP request'
part_423 = """
HTTP request is a request sent to servers. The <strong>request line</strong> \
may look like this:

<span class="code-frame">GET/foo HTTP/1.1</span>

<ul>\
<li class="more-space"><span class="code-frame">GET</span> is a method - a \
type of request we make to the server.</li>\
<li class="more-space"><span class="code-frame">/foo</span> is a path.</li>\
<li class="more-space"><span class="code-frame">HTTP/1.1</span> is a version \
(1.1 is a version number).</li>\
</ul>

There are many request methods, but the most common is GET. An example of \
another method is POST.

The request line is followed by headers. The format of a header is: 

<span class="code-frame">Name: Value</span> like e. g. <span class="code-frame">\
Host: www.example.com</span>.    
"""

title_424 = 'HTTP response'
part_424 = """
HTTP response is what servers send back after recieving the HTTP request. \
The <strong>response line</strong> may look like this:

<span class="code-frame">HTTP/1.1 200 OK</span>\

where <span class="code-frame">200</span> is a <strong>status code</strong>. \
Look at <a href="https://en.wikipedia.org/wiki/List_of_HTTP_status_codes">\
this page</a> for a <b>list of possible HTTP status codes</b> and what they \
mean.
"""
title_425 = 'Web Applications'
part_425 = """
There are two main types of responses servers send back:

<ul>\
<li><strong>static</strong> - a pre/written file that server just returnes \
(e. g. image)</li>\
<li><strong>dynamic</strong> - made on the fly by programs called <strong>web \
applications</strong>.</li>\
</ul>

A <strong>Web Application</strong> is a program that lives on a webserver, \
speaks HTTP and generates requested content.
"""

# Stage 4, Lesson 3:

S4L3 = '3. HTML Forms'

title_431 = 'A structure of HTML form'
part_431 = """
HTML forms are used to collect user input. Their basic structure is following:

<table class="code-frame">\
<tr>\
<td><pre>&lt;form&gt;<br>\
    &lt;input ... &gt;<br>\
    &lt;input ... &gt;<br>\
    .<br>\
    .<br>\
    .<br>\
&lt;/form&gt;</pre></td>\
</tr>\
</table>\
"""

title_432 = 'Form elements'
part_432 = """
The <span class="code-frame">&lt;form&gt;</span> element is the html element \
that packs all the form elements of one form to one group.

There are other form elements inside the &lt;form&gt; element. The most \
important of them is the <span class="code-frame">&lt;input&gt;</span> element.

The &lt;input&gt; element can take a couple of <b>attributes</b>, such as name, \
type or action. 

The &lt;input&gt; element has many variations, depending on the <strong>type \
attribute</strong>, e. g.:

<ul>\
<li>text</li>\
<li>radio</li>\
<li>submit</li>\
</ul>

For better understandig of <b>form elements</b> and <b>creating html forms</b>, \
look at <a href="http://www.w3schools.com/html/html_forms.asp">this page</a>.
""" 

title_433 = 'Input Validation'
part_433 = """
We have to remember that not all users fill in the forms with inputs that are \
desirable. Maybe nothing seriously bad happens, but <b>some inputs can cause \
big problems</b>.

<strong>Validating</strong> user input is <b>to ensure that input is safe</b> \
prior to use.

Anyway, even if the input is not dangerous, it is obviously useful not to \
accept invalid date inputs, invalid e-mail inputs, empty imputs etc.

Input validation is <b>useful also for users</b> if it not only validates the \
data, but also brings some feedback to users. Users usually enter invalid data \
unintentionally so they should get some message about it and get a chance \
to fill in the form again correctly. Otherwise, they don't know what is wrong \
or sometimes even don't know that something is wrong.

<b>Therefore, validation steps should be following</b>:

<ol>\
<li>Verify the users input.</li>\
<li>On error, render form again.</li>\
<li>Include error message</li>\
</ol>

A feedback makes forms to be responsive and that <b>improves the user \
experience</b>.
"""

title_434 = 'HTML Escaping'
part_434 = """
A special attention has to be paid to inputs, which include <span class=\
"code-frame">&lt;</span>, <span class="code-frame">&gt;</span>, <span class=\
"code-frame">&amp;</span> or <span class="code-frame">&quot;</span>.

All these characters are used in html documents for certain reasons. Therefore, \
after submitting input containing these characters, the input may become a part \
of our html code and destroy it, or give the input a style that is not desirable.

Avoiding this problem is called <strong>html escaping</strong> and there are \
more ways how to do it.
"""

# Stage 4, Lesson 4:

S4L4 = '4. HTML Templates'

title_441 = 'A Template'
part_441 = """
A <strong>template</strong> is a piece of code that is written once and then \
<b>repeatedly used</b> for several parts of a webpage. These parts have \
different content, but they are generated by the same code.
"""

title_442 = 'Avoiding repetition'
part_442 = """
The previous definition indicates, that the main advatage of using templates \
in programming is <strong>avoiding repetition</strong>.

<h3 class="gama">When to use templates?</h3>

Webpages often have parts with different content but with the same structure \
and the same style. This webpage is also an example of such a webpage. It has \
several different lessons, but their structure and style are uniform. \
Therefore, it was good to generate their html by a template rather than to \
write the same html code manually for every lesson.

Another example of a good reason for using a template is pasting users inputs \
to a webpage. For example, if we allow users add comments, every submitted \
comment can be pasted to a webpage using the same template.  

<h3 class="gama">Importance of avoiding repetition</h3>

<ul>\
<li>saves time</li>\
<li>reduces making errors</li>\
<li>allows to write/change codes more efficiently</li>\
</ul>
"""

title_443 = 'Jinja2'
part_443 = """
<strong>Jinja2</strong> is a <em>templating engine</em> for Python. Using \
Jinga2 is better way of making templates than writing them directly into a \
Python file.

Look at <a href="http://jinja.pocoo.org/docs/dev/#">this page</a> to find out \
more about Jinja2.
"""

title_444 = 'Template Inheritance'
part_444 = """
Jinja2 allows <strong>template inheritance</strong>, which means that child \
templates inherit from their parent templates.

For example, it can be used in case we want the subpages generated by a child \
template to have the same header and the same footer as the page generated by \
its parent template.
"""

# Stage 4, Lesson 5:

S4L5 = '5. Databases'

title_451 = 'A Database'
part_451 = """
A <strong>database</strong> is an organized collection of data. In programming \
a database is also a program that stores and retrieves the data.

If we allow users to enter inputs to our page, we need to store somehow the \
data we collected from them. Otherwise, the data would be only temporary. \
Databases solve this problem. 
"""

title_452 = 'Types of Databases'
part_452 = """
The major types of databases are:

<ul>\
<li>Relational databases (SQL): Postgresql, MySQL, SqLite, Oracle</li>\
<li>Google App Engine's Datastore</li>\
<li>Amazon Dynamo</li>\
<li>NoSQL</li>\
</ul>
"""

title_453 = "Google App Engine's Datastore"
part_453 = """
This page uses a database of Google App Engine which is called Google App \
Engine's Datastore. 

<a href="https://cloud.google.com/appengine/docs/python/gettingstartedpython27/\
usingdatastore">Here</a> is the tutorial for using this database.
"""

# ------------------------------------------------------------------------------------

# Stage 5:

stage_5 = 'Stage 5'
title_5 = 'Choose Your Next Steps'
description_5 = """\
The goal of Stage 5 is to <b>explore</b> further programming topics. Every \
student is allowed to choose one of the following topics to explore: making \
pages look good, JavaScript, Back End Functionality, Mobile App Development, \
advanced Python. I chose <strong>JavaScript</strong>, so if you read more, \
you will find notes on this topic including the knowledge demonstration. 
"""

# Stage 5, Lesson 1:

S5L1 = '1. JavaScript'

title_511 = 'What is JavaScript?'
part_511 = """
<strong>JavaScript</strong> is programming language. Alongside HTML and CSS, \
it is one of the three essential technologies needed for front-end web \
development. While HTML is used to make the page structure and CSS to make the \
page style, <b>JavaScript is used to make pages come alive</b>.

The following parts are the summary of the <b><a href="https://www.udacity.com/\
course/javascript-basics--ud804">Udacity course JavaScript Basics</a></b>.
"""

title_512 = 'Console'
part_512 = """
While in Python programming we can see what the code is doing directly in the \
text editor, <b>we need a browser to see what a JavaScript code is doing</b>. \
There is a <em>Console</em> folder in <em>Developer Tools</em> which shows the \
results if we use a <span class="code-frame">console.log()</span> function in \
a javascript file.
"""

title_513 = 'Selectors, Variables, If Statements, Loops, Functions ...'
part_513 = """
Like CSS, also JavaScript uses selectors. While in CSS selector determines the \
html element that is going to be styled, in JavaScript selector determines the \
html element that is going to be manipulated.

Similarly to other programming languages (like Python), JavaScript uses \
variables, if statements, while loops, for loops, functions and so on. Of \
course, the syntax is different. 
"""

title_514 = 'JSON'
part_514 = """
<strong>JSON</strong> (JavaScript Object Notation) is a popular and simple \
format for storing and transferring nested or hierarchal data. See these links \
for more details: 

<ul>\
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/\
Global_Objects/JSON"><b>MDN</b></a></li>\
<li><a href="http://json.org/"><b>JSON.org</b></a></li>\
</ul>

It is easy to make mistakes with JSON, therefore it is useful to copy and \
paste a code to <a href="http://jsonlint.com/"><b>JSON linter</b></a> and find \
syntax errors this way.
"""

# Stange 5, Lesson 2:

S5L2 = '2. jQuery'

title_521 = 'What is jQuery?'
part_521 = """
<strong>jQuery is a JavaScript library</strong>  designed to simplify the \
client-side scripting of HTML. It is the most popular JavaScript library in \
use today.

It makes things like HTML document traversal and manipulation, event handling, \
animation, and Ajax much simpler with an easy-to-use API that works across a \
multitude of browsers.

The following parts are a summary of the Udacity course <b><a href="https://\
www.udacity.com/course/intro-to-jquery--ud245">Intro to jQuery</a></b>
"""

title_522 = 'What is jQuery in practice?'
part_522 = """
If we ask what jQuery is according to how it behaves, the answer is very \
simple: <b>jQuery is a JavaScript object</b>.
"""

title_523 = 'jQuery collection'
part_523 = """
jQuery returns an array like object called <strong>jQuery collection</strong>. \
It is an object that looks and behaves like an array, but it includes some \
additional methods.

There are several possibilities of what can be passed into jQuery object:

<ul>\
<li class="more-space">a string <span class="code-frame">$(string)</span></li>\
<li class="more-space">a function <span class="code-frame">$(function)</span>\
</li>\
<li class="more-space">a DOM Element <span class="code-frame">$(DOM Element)\
</span></li>\
<li class="more-space">or we can call methods directly on the jQuery object \
<span class="code-frame">$.ajax()</span></li>\
</ul>
"""

title_524 = 'Adding jQuery to a website'
part_524 = """
To add jQuery to any website, we have to use <span class="code-frame">&lt;\
script&gt;</span> tags.
"""

title_525 = 'Hosting jQuery'
part_525 = """
Possible ways to host jQuery:

<ul>
<li class="more-space"><b>local</b><br><span class="code-frame">&lt;script \
src='js/jquery.min.js'&gt;&lt;/script&gt;</span></li>\
<li class="more-space"><b>jQuery official</b><br><span class="code-frame">\
&lt;script src='//code.jquery.com/jquery-1.11.1.min.js'&gt;&lt;/script&gt;\
</span></li>\
<li class="more-space"><b>Content Delivery Network</b> (recommended)<br>\
<span class="code-frame">&lt;script src='//ajax.googleapis.com/ajax/libs/\
jquery/1.11.1/jquery.min.js'&gt;&lt;/script&gt;</span></li>\
</ul>   

<span class="code-frame">min</span> stands for &quot;minified&quot; and means \
that it is the minified version of jquery. The minified version is considerably \
smaller and leads to faster page loads.
"""

title_526 = 'Selectors'
part_526 = """
In a piece of code like this:

<span class="code-frame">$('string')</span>

the string inside brackets is a <strong>selector</strong> by which we choose \
an html element. The selector may be a tag  <span class="code-frame">$('tag')\
</span>, a class <span class="code-frame">$('.class')</span> or an id  <span \
class="code-frame">$('#id')</span>.
"""

title_527 = 'DOM navigation methods'
part_527 = """
For navigation troughout the DOM we use <strong><a href="http://api.jquery.com/\
category/traversing/">Traversing</a></strong> and <strong><a href="http://api.\
jquery.com/category/traversing/filtering/">Filtering</a></strong>. Using them \
is another way how to get the elements we want. Click the links to learn more.
"""

title_528 = 'DOM manipulation methods'
part_528 = """
Selectors and navigaton methods allow us only to find the right element we \
want to manipulate. To manipulate them, we have to use <b>manipulating methods\
</b>. To learn more about them look at <a href="http://api.jquery.com/"><b>\
this page</b></a>.

The methods descirbed there allow us to do such things as toggling classes, \
changing attributes, modifying CSS, pulling html and text, collecting values, \
adding and removing DOM elements, etc.
"""

title_529 = 'Advantages and disadvantages of jQuery'
part_529 = """
<b>Advantages:</b>

<ul>\
<li>Fast Selection</li>\
<li>Easy DOM Manipulation</li>\
<li>Cross Browser Compatibility</li>\
</ul>

<b>Disadvantage:</b>

jQuery adds a few kBs to the size of a webpage, therefore it may lead to a \
slower page load. This problem can be solved by using <b>CDN</b>.
"""

# Stage 5, Lesson 3:

S5L3 = '3. Demonstrating my new knowledge'

title_531 = 'Animation with .animate()'
part_531 = """
One of the main goals of the course <b>Intro to jQuery</b> was to learn how \
to understand the jQuery API documentation. Since I was always interested in \
how animations on websites are done, I was looking for methods that cause \
animation. 

And I found <span class="code-frame">.animate()</span>. I studied how it works \
(in the jQuery API documentation and in other resources) and how to combine it \
with other functions. I tried to do my own simple animation and ...

<b>here is the result</b>:

<button class="start">Move the Car</button>

<button class="back">Back</button>

<div class="animation">\
<img src="static/images/car2.jpg" alt="car" class="car">\
</div>

<b>Other functions I used for this animation:</b>

The <span class="code-frame">.click()</span> function allowed me to assigne \
what will happen after clicking an appropriate button.

Using <span class="code-frame">.css()</span> function I set the car position \
to 'relative' so that it started to move from the left side of the white box \
(and not from the left edge of the monitor).

I used <span class="code-frame">.one()</span> function to make it impossible \
to move the car out from the monitor by repetitive clicking on <span class=\
"code-frame">Move the Car</span> button. 

I also used <span class="code-frame">location.reload()</span> function \
to reload the page after clicking the <span class="code-frame">Back</span> \
button. This way the car returns to the starting position and we can reuse \
the <span class="code-frame">Move the Car</span> button without reloading \
the page with the browser reload button.
"""


# -------------------------- Helper Function -----------------------------------------


# Every lesson part is a one string text, but some of them have more paragraphs. I want 
# them to be more paragraphs also in the html code, but as one string it would be taken
# as one paragraph by a template. This function takes a string as an input and it returns 
# a list of paragaraphs of the string.

def paragraph_list(string):
    # make a list of paragraphs
    paragraphs = string.splitlines()
    while "" in paragraphs:
        paragraphs.remove("")
    
    # determine, which of the elements in the list paragraphs we don't want to 
    # recieve <p> tags, because they have another tags already:
    non_paragraph = ['<ul', '<ol', '<img', '<h3', '<table', '<div', '<button']
    for element in paragraphs:
        element_index = paragraphs.index(element)
        paragraphs[element_index] = [element] + [True]
        for string in non_paragraph:
            if element.find(string) != -1:
                paragraphs[element_index][1] = False
    return paragraphs

    # the template in lesson.html will evaluate if the element has to recieve <p> tags
    # or not, according to the value True or False.



# -------------------------- List of all lessons --------------------------------------


STAGE_1 = [[S1L1, [[title_111, paragraph_list(part_111)], 
                   [title_112, paragraph_list(part_112)], 
                   [title_113, paragraph_list(part_113)], 
                   [title_114, paragraph_list(part_114)]]],
           [S1L2, [[title_121, paragraph_list(part_121)], 
                   [title_122, paragraph_list(part_122)], 
                   [title_123, paragraph_list(part_123)], 
                   [title_124, paragraph_list(part_124)]]],
           [S1L3, [[title_131, paragraph_list(part_131)], 
                   [title_132, paragraph_list(part_132)], 
                   [title_133, paragraph_list(part_133)], 
                   [title_134, paragraph_list(part_134)],
                   [title_135, paragraph_list(part_135)],
	               [title_136, paragraph_list(part_136)]]]]


STAGE_2 = [[S2L1, [[title_211, paragraph_list(part_211)], 
                   [title_212, paragraph_list(part_212)], 
                   [title_213, paragraph_list(part_213)],
                   [title_214, paragraph_list(part_214)],
                   [title_215, paragraph_list(part_215)],
                   [title_216, paragraph_list(part_216)]]],
           [S2L2, [[title_221, paragraph_list(part_221)], 
                   [title_222, paragraph_list(part_222)]]],
           [S2L3, [[title_231, paragraph_list(part_231)], 
                   [title_232, paragraph_list(part_232)],
                   [title_233, paragraph_list(part_233)],
                   [title_234, paragraph_list(part_234)],
                   [title_235, paragraph_list(part_235)]]],
           [S2L4, [[title_241, paragraph_list(part_241)], 
                   [title_242, paragraph_list(part_242)],
                   [title_243, paragraph_list(part_243)],
                   [title_244, paragraph_list(part_244)],
                   [title_245, paragraph_list(part_245)],
                   [title_246, paragraph_list(part_246)],
                   [title_247, paragraph_list(part_247)]]],
           [S2L5, [[title_251, paragraph_list(part_251)], 
                   [title_252, paragraph_list(part_252)]]]]


STAGE_3 = [[S3L1, [[title_311, paragraph_list(part_311)]]]]


STAGE_4 = [[S4L1, [[title_411, paragraph_list(part_411)], 
                   [title_412, paragraph_list(part_412)], 
                   [title_413, paragraph_list(part_413)]]],
           [S4L2, [[title_421, paragraph_list(part_421)], 
                   [title_422, paragraph_list(part_422)], 
                   [title_423, paragraph_list(part_423)], 
                   [title_424, paragraph_list(part_424)],
                   [title_425, paragraph_list(part_425)]]],
           [S4L3, [[title_431, paragraph_list(part_431)], 
                   [title_432, paragraph_list(part_432)],
                   [title_433, paragraph_list(part_433)],
                   [title_434, paragraph_list(part_434)]]],
           [S4L4, [[title_441, paragraph_list(part_441)], 
                   [title_442, paragraph_list(part_442)],
                   [title_443, paragraph_list(part_443)],
                   [title_444, paragraph_list(part_444)]]],
           [S4L5, [[title_451, paragraph_list(part_451)], 
                   [title_452, paragraph_list(part_452)],
                   [title_453, paragraph_list(part_453)]]]]


STAGE_5 = [[S5L1, [[title_511, paragraph_list(part_511)],
                   [title_512, paragraph_list(part_512)],
                   [title_513, paragraph_list(part_513)],
                   [title_514, paragraph_list(part_514)]]],
           [S5L2, [[title_521, paragraph_list(part_521)],
                   [title_522, paragraph_list(part_522)],
                   [title_523, paragraph_list(part_523)],
                   [title_524, paragraph_list(part_524)],
                   [title_525, paragraph_list(part_525)],
                   [title_526, paragraph_list(part_526)],
                   [title_527, paragraph_list(part_527)],
                   [title_528, paragraph_list(part_528)],
                   [title_529, paragraph_list(part_529)]]],
           [S5L3, [[title_531, paragraph_list(part_531)]]]]

STAGES = [[stage_1, title_1, description_1, STAGE_1],
          [stage_2, title_2, description_2, STAGE_2],
          [stage_3, title_3, description_3, STAGE_3],
          [stage_4, title_4, description_4, STAGE_4],
          [stage_5, title_5, description_5, STAGE_5]]














