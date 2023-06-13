import React from 'react'; 
import axios from "axios"
import DroppableFile from './DroppableFile';
import styles from "../css/pdfUpload.module.css"
import config from "../config"

export default class PdfUpload extends React.Component {

    constructor(props){
        super(props);

        this.state = {
            callback:props.callback
        }
    }

    uploadPdf = (file) => {
    
        if(file == null){
            console.log("no file has been uploaded");
            return;
        }
        axios({
            method:"post",
            url:`${config.API_KEY}/pdf-upload`,
            responseType:'arraybuffer',
            data:file
        }).then(response => {

            let blob = new Blob([response.data], {type:"application/pdf"})
            this.state.callback(blob)    
        })
    }

    render(){

        return(  
            <div className={styles.drop}>
                <DroppableFile 
                    getData={(file) => this.uploadPdf(file)}
                />
            </div>      
        )
    }
}