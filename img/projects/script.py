import os

str = """<li data-masterspeed="400" data-slotamount="7" data-transition="papercut">
    <img src="img/projects/%s" alt=""/>
</li>
"""

for file in os.listdir("."):
    if file.endswith(".jpg"):
        name = os.path.splitext(file)[0]
        print str % (file)

# print str
