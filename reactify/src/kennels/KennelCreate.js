import React, {Component} from 'react'
import KennelForm from "./KennelForm";


class KennelCreate extends Component {
    render() {
        return (
            <div>
                <h1>Create Kennel</h1>
                <KennelForm/>
            </div>
        )
    }
}

export default KennelCreate


// left for reference


//
// class KennelCreate extends Component {
//
//     constructor(props) {
//         super(props);
//         this.handleSubmit = this.handleSubmit.bind(this);
//         this.handleInputChange = this.handleInputChange.bind(this);
//         this.clearForm = this.clearForm.bind(this);
//         this.kennelTitleRef = React.createRef();
//         this.state = {
//             type: 'dogs',
//             title: null,
//             errors: {},
//         };
//     }
//
//
//     createKennel(data) {
//         const endpoint = '/api/kennels/';
//         const csrfToken = cookie.load('csrftoken');
//         let thisComp = this;
//
//         if (csrfToken !== undefined) {
//             let lookupOptions = {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                     'X-CSRFToken': csrfToken  // field name from Django docs
//                 },
//                 body: JSON.stringify(data),
//                 credentials: 'include'
//             };
//
//             fetch(endpoint, lookupOptions)
//                 .then(function (response) {
//                     return response.json()
//                 }).then(function (responseData) {
//                 console.log(responseData);
//                 if (thisComp.props.newKennelItemCreated) {
//                     thisComp.props.newKennelItemCreated(responseData)
//                 }
//                 thisComp.clearForm();
//             }).catch(function (error) {
//                 console.log("error", error);
//                 alert(error)
//             })
//         }
//
//
//     }
//
//     clearForm(event) {
//         if (event) {
//             event.preventDefault();
//         }
//         console.log(this.state);
//         console.log(this.kennelCreateForm.reset());
//
//         this.kennelCreateForm.reset();
//         console.log(this.state)
//     }
//
//     handleSubmit(event) {
//         event.preventDefault();
//         let data = this.state;
//         this.createKennel(data);
//     }
//
//     handleInputChange(event) {
//         event.preventDefault();
//         let key = event.target.name;
//         let value = event.target.value;
//         if (key === 'title') {
//             if (value.length > 50) {
//                 alert('This title is too long!')
//             }
//         }
//         this.setState({
//             [event.target.name]: event.target.value
//         })
//     }
//
//     componentDidMount() {
//         this.kennelTitleRef.current.focus();
//     }
//
//     render() {
//
//         return (
//             <form onSubmit={this.handleSubmit} ref={(el) => this.kennelCreateForm = el}>
//                 <div className='form-group'>
//                     <input type='text'
//                            id='title'
//                            name='title'
//                            className="form-control"
//                            placeholder="Kennel title"
//                            ref={this.kennelTitleRef}
//                            onChange={this.handleInputChange}
//                            // value='test'
//                            required='required'/>
//                 </div>
//                 <div className='form-group'>
//                     <select id='type' name='type' onChange={this.handleInputChange} required='required'>
//                         <option value="dogs">dogs</option>
//                         <option value="cats">cats</option>
//                     </select>
//                 </div>
//                 <button className='btn btn-primary'>Save</button>
//                 <button className='btn btn-secondary' onClick={this.clearForm}>Cancel</button>
//             </form>
//         )
//     }
// }
//
// export default KennelCreate;