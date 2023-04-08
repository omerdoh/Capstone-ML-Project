import React from 'react'; 
import axios from "axios"

export default class PdfUpload extends React.Component {


    constructor(props){
        super(props);

        this.state = {
            file:null
        }
    }


    handleUploadClick = (event) =>{

        let _file = event.target.files[0];
        this.setState({file:_file})
    }

    uploadPdf = (event) => {
        
        event.preventDefault();

        const formData = new FormData();
        formData.append('file', this.state.file);
        axios({
            method:"post",
            url:"http://localhost:5000/pdf-upload",//temp
            data:formData
        })
    }

    render(){

        return(
           <div>
                <p>{this.state.text}</p>

                <form>
                    <label for="myfile">Select a file:</label>
                    <input
                        type="file" 
                        id="myfile" 
                        name="myfile"
                        onChange={(event) => this.handleUploadClick(event)}
                    />
                </form>

                <button Title="Submit" onClick={(event) => this.uploadPdf(event)}>Upload</button>
           </div> 
        )
    }
}
