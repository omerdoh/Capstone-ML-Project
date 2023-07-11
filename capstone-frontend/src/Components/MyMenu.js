import React from "react";
import { Sidebar, Menu, MenuItem} from 'react-pro-sidebar';

import Home from "../Routes/Home";

//this should be function
export default class MyMenu extends React.Component{

    render(){
        return(
            <Sidebar backgroundColor="#003328" width="10vw" style={{fontFamily:"Gotham-Bold", border:"none"}} onBackdropClick={() => this.props.callback()} toggled={this.props.toggle} breakPoint="all">
                <Menu transitionDuration={300}>
                    <MenuItem onClick={() => this.props.componentToRender(<Home/>)}>Home</MenuItem>
                    <MenuItem 
                    >Algonquin Visual Standards</MenuItem>
                </Menu>
            </Sidebar>
        )
    }
}


