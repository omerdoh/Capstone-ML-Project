import React from 'react'; 
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
            <div style={{ flexDirection: 'column', height: '100vh', width:"100%" }}>
                {(this.state.pdf) ? 
                    <iframe title="title" src={URL.createObjectURL(this.state.pdf)} width="100%" height="100%"></iframe>
                : null}
            </div>
        )
    }
}