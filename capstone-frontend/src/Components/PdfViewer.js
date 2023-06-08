import React from 'react'; 
import { Viewer } from '@react-pdf-viewer/core';
import '@react-pdf-viewer/core/lib/styles/index.css';


export default class PdfViewer extends React.Component{

    constructor(props){
        super(props);

        this.state = {
            pdf:props.pdf
        }
    }

    componentDidMount(){
        //url perhaps
    }

    render(){
        console.log(this.state)
        return(
            <div style={{ display: 'flex', flexDirection: 'column', height: '100vh' }}>
                {(this.state.pdf) ? 
                    <iframe src={URL.createObjectURL(this.state.pdf)} width="50%" height="100%"></iframe>
                : null}
            </div>
        )
    }
}