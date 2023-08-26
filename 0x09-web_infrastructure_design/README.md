User's Computer: This is where the end-users access the web application.
Load Balancer Cluster (HAproxy):
We use a load balancer cluster to distribute incoming requests across multiple servers for improved performance, fault tolerance, and scalability.
Having multiple load balancers provides redundancy in case one fails.
Web Servers:
Web servers (e.g., Nginx or Apache) are responsible for handling HTTP/HTTPS requests and serving static content.
By separating the web server from the application server, we can optimize each component for its specific task.
Application Servers:
Application servers run the application code and logic, generating dynamic content.
Separating the application server from the web server allows for better resource allocation and scalability.
Database Server:
The database server, such as MySQL or PostgreSQL, stores and manages structured data.
Isolating the database on its own server improves data security and scalability.

