import React from "react";

import "../css/about.css"


export default class About extends React.Component {

    constructor(props) {

        super(props);

        this.state = {  

        }
    }
    
    render() { 
        return(
            <div className="container">
                <p>About Us</p>           
            </div>
        );
    }
}