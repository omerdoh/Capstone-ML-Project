import React from "react";
import PdfUpload from "../Components/PdfUpload";
import PdfViewer from "../Components/PdfViewer";
import "../css/home.css"

export default class Home extends React.Component {

    constructor(props) {
        super(props)

        this.state = {
            file: null
        }
    }

    getFile = (fileblob) => {

        this.setState({
            file: null

        }, () => {

            this.setState({
                file: fileblob
            }, () => console.log(this.state.file))
        })
    }

    render() {
        return (
            <div className="Container">

                {this.state.file && <div className="item">
                    {(this.state.file) ? <PdfViewer pdf={this.state.file} /> : <div></div>}
                </div>}

                <div className="item">
                    <PdfUpload callback={(fileblob) => this.getFile(fileblob)} />
                </div>
            </div>
        );
    }
}
