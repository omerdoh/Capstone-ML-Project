import React from 'react'; 
import axios from "axios"
import DroppableFile from './DroppableFile';
import styles from "../css/pdfUpload.module.css"
import config from "../config"

export default class PdfUpload extends React.Component {


    constructor(props){
        super(props);

        this.state = {
            resetState:null,
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
            data:file
        }).then(response => {

        })
    }

    render(){

        return(
           <div className={styles.div}>
            
                <div className={styles.drop}>
                    <DroppableFile 
                        getData={(file) => this.uploadPdf(file)}
                    />
                </div>      
           </div> 
        )
    }
}