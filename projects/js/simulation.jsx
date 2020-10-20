import React from 'react';

class Simulation extends React.Component {
  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = { command: '', output: '' };
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
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

    const commandUrl = `/api/simulation/${this.state.command}`;
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
      .catch(error => console.log(error));// eslint-disable-line no-console

    event.preventDefault();
    event.target.reset();
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
      <div id="parent">
        <form onSubmit={this.handleSubmit} id="input-form">
          <input type="text" value={this.state.value} onChange={this.handleChange} />
          <input type="submit" value="send" />
          <a href="../static/commands/simulation_commands.txt" target="_blank"> commands </a>
          <a href="../static/commands/simulation_README.md" target="_blank"> README </a>
          <a href="https://github.com/chanchoi829/simulation" target="_blank"> GitHub </a>
        </form>
        <a href="http://157.230.189.229/api/simulation" target="_blank">start simulation api ONLY CLICK ON THIS AFTER YOU TYPE "quit"</a>
        {display}
      </div>
    );
  }
}

export default Simulation;
