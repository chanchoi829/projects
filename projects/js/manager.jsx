import React from 'react';
import '../static/css/projects.css';


class Manager extends React.Component {
  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = { command: '', output: '' };
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.handleNothing = this.handleNothing.bind(this);
  }

  componentDidMount() {
  }

  handleChange(event) {
    this.setState({ command: event.target.value });
  }

  handleSubmit(event) {
    this.setState({ command: event.target.value });
    if (this.state.command === '') {
      return;
    }
    const commandUrl = `/api/manager/${this.state.command}`;
    setTimeout(() => {
      
      fetch(commandUrl, { credentials: 'same-origin' })
        .then((response) => {
          if (!response.ok) throw Error(response.statusText);
          return response.json();
        })
        .then((data) => {
          this.setState({
            output: data.output,
          });
        })
        .catch(error => console.log(error));
    }, 2000);
    // eslint-disable-line no-console

    event.preventDefault();
    event.target.reset();
  }

  handleNothing(event) {
    event.preventDefault();
  }

  render() {
    if (!this.state) {
      setTimeout(this.render, 1);
      return null;
    }

    let display = [];
    let tmp = '';
    for(let i = 0; i < this.state.output.length; i++) {
      if (this.state.output[i] === '\n') {
        display.push(tmp);
        display.push(<br></br>);
        tmp = '';
      }
      else {
        tmp += this.state.output[i];
      }
    }
    display.push(tmp);
    display.push(<br></br>);
    return (
      <div class="parent">
        <div class="left">
          Media Manager!
          <form onSubmit={this.handleSubmit} id="input-form">
            <input type="text" value={this.state.value} onChange={this.handleChange} />
            <input type="submit" value="send" />
          </form>
          <a href="http://www.chanchoi829.com/api/manager" target="_blank">Click me after "quit"</a>
          {display}
        </div>
        <div class="right">
          Example Usage:
          <form onSubmit={this.handleNothing} id="input-form">
            <input type="text" value="open_map_view" />
            <input type="submit" value="send" />
          </form>
          <form onSubmit={this.handleNothing} id="input-form">
            <input type="text" value="show" />
            <input type="submit" value="send" />
          </form>
          <form onSubmit={this.handleNothing} id="input-form">
            <input type="text" value="status" />
            <input type="submit" value="send" />
          </form>
          <form onSubmit={this.handleNothing} id="input-form">
            <input type="text" value="Ajax position 25 25 20" />
            <input type="submit" value="send" />
          </form>
          <form onSubmit={this.handleNothing} id="input-form">
            <input type="text" value="Valdez load_at Shell" />
            <input type="submit" value="send" />
          </form>
          <form onSubmit={this.handleNothing} id="input-form">
            <input type="text" value="create Chan Cruiser 20 26" />
            <input type="submit" value="send" />
          </form>
          <form onSubmit={this.handleNothing} id="input-form">
            <input type="text" value="go" />
            <input type="submit" value="send" />
          </form>
          <form onSubmit={this.handleNothing} id="input-form">
            <input type="text" value="show" />
            <input type="submit" value="send" />
          </form>
          <form onSubmit={this.handleNothing} id="input-form">
            <input type="text" value="Ajax attack Xerxes" />
            <input type="submit" value="send" />
          </form>
          <form onSubmit={this.handleNothing} id="input-form">
            <input type="text" value="go" />
            <input type="submit" value="send" />
          </form>
          <form onSubmit={this.handleNothing} id="input-form">
            <input type="text" value="show" />
            <input type="submit" value="send" />
          </form>
          <form onSubmit={this.handleNothing} id="input-form">
            <input type="text" value="quit" />
            <input type="submit" value="send" />
          </form>
          <br></br>
          After you quit, click on "Click me after quit" to restart! <br></br>
          There are more commands :) Check the links below <br></br><br></br>
          <a href="../static/commands/manager_commands.txt" target="_blank"> Commands </a>
          <br></br>
          <a href="../static/commands/manager_README.md" target="_blank"> README </a>
          <br></br>
          <a href="https://github.com/chanchoi829/manager" target="_blank"> GitHub </a>
          <br></br>
          <br></br>
          You can do multiple commands at once
          <form onSubmit={this.handleNothing} id="input-form">
            <input type="text" value="open_map_view show status" />
            <input type="submit" value="send" />
          </form>
          WARNING: "quit" should always be alone!
        </div>
      </div>
    );
  }
}

export default Manager;
