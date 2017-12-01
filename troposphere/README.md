         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Hi there! Welcome to AWS Cloud9!

To get started, create some files, play with the terminal,
or visit https://docs.aws.amazon.com/console/cloud9/ for our documentation.

Happy coding!

Troposphere install guide for AWS Cloud9

1. Spin up a c9 instance (in a public subnet) and ensure SSH inbound rule is locked down
2. sudo yum install git -y
3. git config --global user.name "USERNAME"
4. git config --global user.email "EMAIL"
5. git clone https://github.com/REPO
6. sudo yum -y install python-pip
7. sudo pip install troposphere
8. sudo yum update -y
9. code, commit, push :)