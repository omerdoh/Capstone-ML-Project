import React from "react";
import PdfUpload from "./Components/PdfUpload";
import PdfViewer from "./Components/PdfViewer";
import styles from "./css/app.module.css"


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

        <div className={styles.Container}>

          <div className={styles.pdfViewer}>
            {(this.state.file) ? <PdfViewer pdf={this.state.file} />: <div></div>}
          </div>  

          <div className={styles.pdfUpload}>
            <PdfUpload callback={(fileblob) => this.getFile(fileblob)} />
          </div>      
        </div>
    </div>
    );
  }
}

//