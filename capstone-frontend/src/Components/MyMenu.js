import React from "react";
import { Sidebar, Menu, MenuItem} from 'react-pro-sidebar';

import Home from "../Routes/Home";
import About from "../Routes/About";

//this should be function
export default class MyMenu extends React.Component{

    render(){
        return(
            <Sidebar backgroundColor="#003328" width="10vw" style={{fontFamily:"Gotham-Bold", border:"none"}} onBackdropClick={() => this.props.callback()} toggled={this.props.toggle} breakPoint="all">
                <Menu transitionDuration={300}>
                    <MenuItem onClick={() => this.props.componentToRender(<Home/>)}>Home</MenuItem>
                    <MenuItem
                        href="https://www.algonquincollege.com/acmarketing/files/2022/12/AC-Visual-Identity-Standards-2023.pdf"
                        target="_blank" 
                        rel="noopener noreferrer"
                    >Algonquin Visual Standards</MenuItem>
                     <MenuItem onClick={() => this.props.componentToRender(<About/>)}>About Us</MenuItem>
                </Menu>
            </Sidebar>
        )
    }
}


