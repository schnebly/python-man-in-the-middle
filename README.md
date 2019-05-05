# python-man-in-the-middle

Man-in-the-middle project written in Python using sockets, threading, and object-oriented programming in order to illustrate the concept of covertly intercepting and modifying messages between two parties in a client-server architecture.

Throughout the course of the project, Alex and James endured some trials and tribulations in order to the get Python program to run as intended. One of the challeneges included understanding the threading implications of the program in order to get all "ends" (client, server, attacker) of the program working at the same time and allowing them to communicate through the sending and receiving of data. One of the idiosyncrasies that the duo encountered was the imperative nature of the `socket` library; having to specify the encoding used to send the data as well as the buffer size was a level of detail that neither James nor Alex were prepared for given the overall declarative paradigm that usually accompanys the language. Once all the necessary functionality was implemented, the code was commented and the output was modified in order to make it easier to understand both from a code perspective and a functionality perspective. Overall, the project was a great learning experience for both Alex and James in the context of cybersecurity and revealed some of the underlying idiosyncracies of communicating in a client-server network especially when there is a man-in-the-middle involved.