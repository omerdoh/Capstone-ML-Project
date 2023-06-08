import React from "react";
import PdfUpload from "./Components/PdfUpload";
import PdfViewer from "./Components/PdfViewer";

export default class App extends React.Component{

  constructor(){
    super()
    this.state = {
      file:null
    }
  }

  getFile = (fileblob) => {
    
    this.setState({
      file:fileblob
    })
  }

  render(){
    return (
      <div className="App">
        <div style={{ display: "flex", flexDirection:"column"}}>
          <PdfUpload callback={(fileblob) => this.getFile(fileblob)}/>
        </div>
        <div>
          {(this.state.file) ? <PdfViewer pdf={this.state.file}/> : null} 
        </div>
      </div>
    );
  }
}