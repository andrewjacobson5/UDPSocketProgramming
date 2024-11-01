# UDPSocketProgramming

This program demonstrates basic UDP communication between a client and a server using sockets. The client sends an integer and a message with its name to the server, and the server responds with its own name and an integer. Both client and server perform actions based on the messages they receive.

### Client
- Accepts an integer input between 1 and 100 from the user.
- Opens a UDP socket and sends a message with:
  - The client’s name.
  - The integer entered by the user.
- Waits for a response from the server.
- Receives and displays:
  - The server’s name.
  - The integer chosen by the server.
  - The sum of both integers.
- Closes the connection upon completion.

### Server
- Opens a UDP socket and listens for incoming client messages.
- When a client message is received:
  - Extracts and displays the client’s name and its own name.
  - Selects an integer between 1 and 100.
  - Displays the client’s integer, the server’s integer, and their sum.
  - Sends a response back to the client with:
    - The server’s name.
    - The integer chosen by the server.
- Shuts down if it receives an out-of-range integer from the client.
