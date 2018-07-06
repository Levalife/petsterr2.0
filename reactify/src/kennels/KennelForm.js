import React, {Component} from 'react'
import cookie from "react-cookies";
import 'whatwg-fetch'

class KennelForm extends Component {

    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleInputChange = this.handleInputChange.bind(this);
        this.clearForm = this.clearForm.bind(this);
        this.kennelTitleRef = React.createRef();
        this.state = {
            type: 'dogs',
            title: null,
            errors: {},
        };
    }

    createKennel(data) {
        const endpoint = '/api/kennels/';
        const csrfToken = cookie.load('csrftoken');
        let thisComp = this;

        if (csrfToken !== undefined) {
            let lookupOptions = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken  // field name from Django docs
                },
                body: JSON.stringify(data),
                credentials: 'include'
            };

            fetch(endpoint, lookupOptions)
                .then(function (response) {
                    return response.json()
                }).then(function (responseData) {
                console.log(responseData);
                if (thisComp.props.newKennelItemCreated) {
                    thisComp.props.newKennelItemCreated(responseData)
                }
                thisComp.clearForm();
            }).catch(function (error) {
                console.log("error", error);
                alert(error)
            })
        }


    }

    updateKennel(data) {
        const {kennel} = this.props;
        const endpoint = `/api/kennels/${kennel.slug}/`;
        const csrfToken = cookie.load('csrftoken');
        let thisComp = this;

        if (csrfToken !== undefined) {
            let lookupOptions = {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken  // field name from Django docs
                },
                body: JSON.stringify(data),
                credentials: 'include'
            };

            fetch(endpoint, lookupOptions)
                .then(function (response) {
                    return response.json()
                }).then(function (responseData) {
                // console.log(responseData);
                if (thisComp.props.kennelItemUpdated) {
                    thisComp.props.kennelItemUpdated(responseData)
                }
            }).catch(function (error) {
                console.log("error", error);
                alert(error)
            })
        }


    }

    clearForm(event) {
        if (event) {
            event.preventDefault();
        }
        this.kennelUpdateForm.reset();
        this.defaultState();
    }

    handleSubmit(event) {
        event.preventDefault();
        let data = this.state;

        const {kennel} = this.props;
        if (kennel !== undefined) {
            this.updateKennel(data);
        } else {
            this.createKennel(data);
        }
    }

    handleInputChange(event) {
        event.preventDefault();
        let key = event.target.name;
        let value = event.target.value;
        if (key === 'title') {
            if (value.length > 50) {
                alert('This title is too long!')
            }
        }
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    defaultState() {
        this.setState({
            title: '',
            type: 'dogs'
        })
    }

    componentDidMount() {
        const {kennel} = this.props;
        if (kennel !== undefined) {
            this.setState({
                type: kennel.type,
                title: kennel.title,
                reg_number: kennel.reg_number,
                about: kennel.about,
                url: kennel.url,
                slug: kennel.slug,
                // 'address',
                // 'timezone',
                skype: kennel.skype,
                facebook: kennel.facebook,
                site: kennel.site,
                // 'owner',
                // 'owner_name',
                country_club: kennel.country_club ? kennel.country_club.id : "",
                // 'country'
            })
        } else {
            this.defaultState()
        }
        // this.kennelTitleRef.current.focus();
    }

    render() {
        const {kennel} = this.props;
        const {title} = this.state;
        const {type} = this.state;
        const {reg_number} = this.state;
        const {slug} = this.state;
        const {about} = this.state;
        const {skype} = this.state;
        const {facebook} = this.state;
        const {site} = this.state;
        const {country_club} = this.state;
        const cancelClass = this.props.kennel !== undefined ? 'd-none' : '';
        return (
            <form onSubmit={this.handleSubmit} ref={(el) => this.kennelUpdateForm = el}>
                <div className='form-group'>
                    <input type='text'
                           id='title'
                           name='title'
                           className="form-control"
                           placeholder="Kennel title"
                           ref={this.kennelTitleRef}
                           onChange={this.handleInputChange}
                           value={title}
                           required='required'/>
                </div>
                <div className='form-group'>
                    <select id='type' name='type' value={type} onChange={this.handleInputChange} required='required'>
                        <option value="dogs">dogs</option>
                        <option value="cats">cats</option>
                    </select>
                </div>
                {kennel !== undefined ?
                    <div className='form-group'>
                    <input type='text'
                           id='reg_number'
                           name='reg_number'
                           className="form-control"
                           placeholder="Kennel registration number"
                           onChange={this.handleInputChange}
                           value={reg_number}
                    />
                    </div>
                : ""}
                {kennel !== undefined ?
                    <div className='form-group'>
                        <input type='text'
                               id='slug'
                               name='slug'
                               className="form-control"
                               placeholder="Kennel page name"
                               onChange={this.handleInputChange}
                               value={slug}
                        />
                    </div>
                : ""}
                {kennel !== undefined ?
                    <select name="country_club" id="country_club" value={country_club}></select>
                : ""}
                {kennel !== undefined ?
                    <div className='form-group'>
                        <input type='text'
                               id='site'
                               name='site'
                               className="form-control"
                               placeholder="Kennel site link"
                               onChange={this.handleInputChange}
                               value={site}
                        />
                    </div>
                : ""}
                {kennel !== undefined ?
                    <div className='form-group'>
                        <input type='text'
                               id='facebook'
                               name='facebook'
                               className="form-control"
                               placeholder="Kennel facebook page"
                               onChange={this.handleInputChange}
                               value={facebook}
                        />
                    </div>
                : ""}
                {kennel !== undefined ?
                    <div className='form-group'>
                        <input type='text'
                               id='skype'
                               name='skype'
                               className="form-control"
                               onChange={this.handleInputChange}
                               value={skype}
                        />
                    </div>
                : ""}
                {kennel !== undefined ?
                    <div className='form-group'>

                        <textarea name="about" id="about" value={about} onChange={this.handleInputChange}></textarea>
                    </div>
                : ""}

                <button className='btn btn-primary'>Save</button>
                <button className={`btn btn-secondary`} onClick={this.clearForm}>Clear</button>
            </form>
        )
    }
}

export default KennelForm;