# Projects
Projects is my webiste which features my two programs: manager and simulation.
You can visit my website here: www.chanchoi829.com
Note: this README is still WIP

### Build Instructions
Git clone:
```bash
$ git clone https://github.com/chanchoi829/projects.git
$ cd projects
```

Create a Python virtual environment:
```bash
$ python3 -m venv env
$ source env/bin/activate
```

Install required Python packages:
```bash
$ pip install .
```

Install ReactJS packages:
```bash
$ npm install .
$ npx webpack
```

Boot up the servers:
```bash
$ ./bin/projectsrun
```

Go to http://localhost:8000/
Click on -> "Click me after quit" to start the middle man API server
Note: you do not need to wait for the api server to close
Start typing commands in the input box.
Have fun!

### Servers

Middle Man API: http://localhost:8000/api/simulation/<string:command>

Execution API: http://localhost:8000/api/simulation

### How It Works

Middle Man API receives commands from clients and delivers them to the Execution API. The commands are then executed on the Execution API. The output is then delivered to clients via Middle Man API.
