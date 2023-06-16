import React from 'react'; 

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
            <div style={{position: "relative", flexDirection: 'column', height: '100%', width:"100%" }}>
                {(this.state.pdf) ? 
                    <iframe 
                        title="title" 
                        src={URL.createObjectURL(this.state.pdf)} 
                        style={{width:"100%", height:"98%"}}>
                    </iframe>
                : null}
            </div>
        )
    }
}