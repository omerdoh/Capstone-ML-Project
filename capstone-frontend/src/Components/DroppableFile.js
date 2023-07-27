//https://medium.com/@650egor/simple-drag-and-drop-file-upload-in-react-2cb409d88929
import React from "react"
import "../css/droppable.css"

export default class DroppableFile extends React.Component{

    constructor(props){
        super(props)

        this.state = {
            fileName:"",
            files:[],
            images:[]
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

        this.removeFile()
        this.handleFileType(e.dataTransfer.files)
    }

    handleClick = (e) => {

        this.removeFile()
        this.handleFileType(e.target.files)
    }

    handleFileType = (files) => {//after uploading a file the file with not change with a different file

        if(files && files.length > 0){//there are files

            let filteredFiles = []
            let filteredImages = []
            let tempFileName = ""

            for (let i = 0; i < files.length; i++) {

                switch(files[i].type){

                    case "application/pdf":
                        filteredFiles.push(files[i])
                        tempFileName = files[i].name
                        break;
                    case "image/jpeg":
                    case "image/png":
                        filteredImages.push(files[i])

                        if(i === 0){
                            tempFileName = files[i].name
                        }else if(i === files.length - 1){
                            tempFileName = tempFileName + "..." + files[i].name
                        }
                        break;
                    default:
                        console.log("the file is not a pdf or image")          
                        break;
                }
            }

            this.setState({
                files:filteredFiles,
                images:filteredImages,
                fileName:tempFileName
            })
        }else{
            console.log("No File");
            return;
        }
    }

    uploadFile = () => {//form data needed
       
        if(this.state.files && this.state.files.length > 0){

            let formData = new FormData()
            this.state.files.forEach(file => {
                formData.append("files", file)
            })
            this.props.getPdfs(formData)
        }
        
        if(this.state.images && this.state.images.length > 0){
            let formData = new FormData()

            //formData.append("images", this.state.images)
            this.state.images.forEach((image, i) => {
                formData.append("images", image)
            })
            this.props.getImgs(formData)
        }
    }
    removeFile = () => {

        this.setState({
            files:null,
            images:null,
            fileName:""
        })
    }

    render(){

        return(

            <div className="DroppableComponent">

                <div className="dropContainer">

                    <div className="drop" ref={this.drop}>
                        {this.props.children}
                        Click&nbsp; 
                        <label htmlFor="file-input" className="uploadText">Upload</label>
                        <input type="file" id="file-input" onClick={(e) => { e.target.value = null }} onChange={(e) => this.handleClick(e)} style={{ display: "none" }} />
                        &nbsp;or Drag and Drop file                      
                    </div>

                    <div className="fileText">

                       {this.state.fileName == "" ? "No File Selected" : this.state.fileName}

                        <input className="removeButton" type="button" id="file-remove" onClick={() => this.removeFile()} value="X"></input>
                    </div>      
                </div>
                <div className="button">
                    <button onClick={() => this.uploadFile()}>Upload Pdf</button>
                </div> 
            </div>

        )
    }
}