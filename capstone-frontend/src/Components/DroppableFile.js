//https://medium.com/@650egor/simple-drag-and-drop-file-upload-in-react-2cb409d88929
import React from "react"
import styles from "../css/droppable.module.css"

export default class DroppableFile extends React.Component{

    constructor(props){
        super(props)

        this.state = {
            fileName:null,
            file:null
        }
    }

    drop = React.createRef()

    componentDidMount(){

        let div = this.drop.current
        div.addEventListener('drop', this.handleDrop)
        div.addEventListener('dragenter', this.handleDragIn)
        div.addEventListener('dragleave', this.handleDragOut)
        div.addEventListener('dragover', this.handleDrag)
    }

    componentWillUnmount() {

        let div = this.drop.current
        div.removeEventListener('drop', this.handleDrop)
        div.removeEventListener('dragenter', this.handleDragIn)
        div.removeEventListener('dragleave', this.handleDragOut)
        div.removeEventListener('dragover', this.handleDrag)
    }

    handleDrag = (e) => {

        e.preventDefault()
        e.stopPropagation()
    }
    handleDragIn = (e) => {

        e.preventDefault()
        e.stopPropagation()
    }
    handleDragOut = (e) => {

        e.preventDefault()
        e.stopPropagation()
    }

    handleDrop = (e) => {   

        e.preventDefault()
        e.stopPropagation()

        if(e.dataTransfer.files && e.dataTransfer.files.length > 0){

            this.setState({
                fileName:e.dataTransfer.files[0].name,
                file:e.dataTransfer.files[0]
            }) 
        }
    }

    handleClick = (e) => {

        console.log(this.state);
        if(!e.target.files[0]){
            console.log("error uploading");
            return;
        }
        this.setState({
            fileName:e.target.files[0].name,
            file:e.target.files[0]
        })
    }

    uploadFile = () =>{
        
        if(this.state.file == null){
            return;
        }
        let formData = new FormData()
        formData.append("file", this.state.file)
        
        this.props.getData(formData)

        this.removeFile()
    }
    removeFile = () => {

        if(this.state.fileName != null){
            this.setState({
                fileName:null,
                file:null
            })
        }
    }

    render(){

        return(

            <div style={{fontFamily:"monospace", width:"15%"}}>

                <div className={styles.dropContainer}>

                    <div className={styles.drop} ref={this.drop}>
                        {this.props.children}
                        Click&nbsp; 
                        <label htmlFor="file-input" className={styles.uploadText}>Upload</label>
                        <input type="file" id="file-input" onClick={(e) => { e.target.value = null }} onChange={(e) => this.handleClick(e)} style={{ display: "none" }} />
                        &nbsp;or Drag and Drop file                      
                    </div>

                    <div className={styles.fileText}>
                       {this.state.fileName == null ? "No File Selected" : this.state.fileName}

                       <div className={styles.removeFile}>

                            <label htmlFor="file-remove" className={styles.uploadText}>X</label>
                            <input type="button" id="file-remove" onClick={this.removeFile} style={{ display: "none" }}/>
                        </div>
                    </div>      
                </div>
                <div className={styles.button}>
                    <button onClick={() => this.uploadFile()}>Upload Pdf</button>
                </div> 
            </div>

        )
    }
}