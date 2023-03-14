import React from 'react';

export default class PdfUpload extends React.Component {


    constructor(props){
        super(props);

        this.state = {

        }
    }


    handleUploadClick = (event) =>{

        let file = event.target.files;
        let text = event.target.result;

        let reader = new FileReader();

        reader.onload = async(text) =>{
            console.log(text.currentTarget.result)
        }
        reader.readAsText(file[0])
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
            
           </div> 
        )

    }

}
