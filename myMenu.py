#!/usr/bin/python

import menu

cowsay = menu.Action("Clever Cow","Inspirational words from a cow.",["/usr/games/fortune | /usr/games/cowsay"])
option1 = menu.Action("Print Hello","Prints 'Hello' to the screen.",["/bin/echo","Hello"])
option1.requireConfirmation = True
option2 = menu.Action("Ping","Pings a given URL.",
  ["/bin/ping"],
  [menu.Parameter("Packet Count","Packets to send.",code="-c",default="4"),
   menu.Parameter("URL","URL to ping.")])
option2.requireConfirmation = True
subMenu = menu.Menu("Submenu", "More stuff.", [option1,option2])

topMenu = menu.Menu("A Menu","Some stuff to do.",[subMenu,cowsay])

topMenu.execute(None,None);
