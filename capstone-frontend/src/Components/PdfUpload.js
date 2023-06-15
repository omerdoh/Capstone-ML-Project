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

    uploadPdf = (files) => {
    
        console.log('====================================');
        console.log("Upload pdf");
        console.log('====================================');

        if(files == null){
            console.log("no file has been uploaded");
            return;
        }
        axios({
            method:"post",
            url:`${config.API_KEY}/pdf-upload`,
            responseType:'arraybuffer',
            data:files
        }).then(response => {

            let blob = new Blob([response.data], {type:"application/pdf"})
            this.state.callback(blob)    
        })
    }

    uploadImgs = (images) => {

        console.log('====================================');
        console.log("Upload image");
        console.log('====================================');
        axios({
            method:"post",
            url:`${config.API_KEY}/img-upload`,
            responseType:'arraybuffer',
            data:images
        }).then(response => {


            console.log(response.data)
            //let blob = new Blob([response.data], {type:"application/pdf"})
            //this.state.callback(blob)    
        })
    }

    render(){

        return(  
            <div className={styles.drop}>
                <DroppableFile 
                    getPdfs={(files) => this.uploadPdf(files)}
                    getImgs={(images) => this.uploadImgs(images)}
                />
            </div>      
        )
    }
}