import React from "react";
import Header from "../Components/Header";
import "../css/app.css"
import Home from "./Home";

export default class App extends React.Component{

  constructor(props){
    super(props)

    this.state = {
      component:null
    }
  }

  renderCallback = (_component) => {

    this.setState({
      component:_component
    })
  }

  render(){
    return (
      <div className="App">
        <Header renderCallback={(component) => this.renderCallback(component)}/>
        
        {this.state.component === null ? <Home/> : <>{this.state.component}</>}
      </div>
    );
  }
}