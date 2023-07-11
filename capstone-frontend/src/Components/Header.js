import React from 'react';
import MyMenu from '../Components/MyMenu';
import "../css/header.css"

export default class Header extends React.Component{

  constructor(props){
    super(props)

    this.state = {
      toggleMenu:false,
    }
  }

  toggleMenu = () => {
    this.setState({
      toggleMenu:!this.state.toggleMenu
    })
}

  render(){

    return (
      <div className="header">
        <button className="hamburger-button" onClick={() => this.toggleMenu()}>☰</button>  

        <img className='image' alt="" src="AlgonquinCollegeIcon.png"/>
        <MyMenu componentToRender={(component) => this.props.renderCallback(component)} toggle={this.state.toggleMenu} callback={() => this.toggleMenu()}/>
      </div>
    );
  }
}
