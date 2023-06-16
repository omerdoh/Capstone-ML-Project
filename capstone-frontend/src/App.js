import React from "react";
import PdfUpload from "./Components/PdfUpload";
import PdfViewer from "./Components/PdfViewer";
import Header from "./Components/Header";
import styles from "./css/app.module.css"


export default class App extends React.Component{

  constructor(props){
    super(props)

    this.state = {
      file:null
    }
  }

  getFile = (fileblob) => {

    this.setState({
      file:null

    }, () => {

      this.setState({
        file:fileblob
      })
    })
  }

  render(){
    return (
      <div className="App">

        <Header />

        <div className={styles.Container}>

          
          {this.state.file && <div className={styles.pdfViewer}>
            {(this.state.file) ? <PdfViewer pdf={this.state.file} />: <div></div>}
          </div>}

          <div className={styles.pdfUpload}>
            <PdfUpload callback={(fileblob) => this.getFile(fileblob)} />
          </div>     
        </div>
      </div>
    );
  }
}

