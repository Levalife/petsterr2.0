import React, {Component} from 'react';
import {Link} from 'react-router-dom'

import 'whatwg-fetch'
import cookie from 'react-cookies'

import KennelForm from './KennelForm';

import KennelInList from "./KennelInList";

class Kennels extends Component {
    constructor(props) {
        super(props);
        this.toggleKennelListClass = this.toggleKennelListClass.bind(this);
        this.handleNewKennel = this.handleNewKennel.bind(this);
        this.loadMoreKennels = this.loadMoreKennels.bind(this);
    }

    state = {
        kennels: [],
        kennelsListClass: 'card',
        next: null,
        previous: null,
        registered_user: false,
        count: 0
    };

    loadMoreKennels() {
        const {next} = this.state;
        if (next !== null && next !== undefined) {
            this.loadKennels(next)
        }
    }

    loadKennels(nextEndpoint) {
        let endpoint = '/api/kennels/';
        if (nextEndpoint !== undefined) {
            endpoint = nextEndpoint
        }
        let thisComp = this;
        let lookupOptions = {
            method: "GET",
            headers: {
                'Content-Type': 'application/json'
            },
        };

        const csrfToken = cookie.load('csrftoken');
        if (csrfToken !== undefined) {
            lookupOptions['credentials'] = 'include';
            lookupOptions['headers']['X-CSRFToken'] = csrfToken;
        }

        fetch(endpoint, lookupOptions)
            .then(function (response) {
                return response.json()
            }).then(function (responseData) {
            // let currentKennels = thisComp.state.kennels;
            // let newKennels = currentKennels.concat(responseData.results);
            thisComp.setState({
                kennels: thisComp.state.kennels.concat(responseData.results),
                next: responseData.next,
                previous: responseData.previous,
                registered_user: responseData.registered_user,
                count: responseData.count
            })
        }).catch(function (error) {
            console.log("error", error)
        })
    }

    handleNewKennel(kennelItemData) {
        let currentKennels = this.state.kennels;
        currentKennels.push(kennelItemData);
        this.setState({
            kennels: currentKennels
        })
    }


    toggleKennelListClass(event) {
        event.preventDefault();
        let currentListClass = this.state.kennelsListClass;
        if (currentListClass === "") {
            this.setState({
                kennelsListClass: 'card',
            });
        } else {
            this.setState({
                kennelsListClass: '',
            });
        }

    }

    componentDidMount() {
        this.setState({
            kennels: [],
            kennelsListClass: 'card',
            next: null,
            previous: null,
            registered_user: false,
            count: 0
        });
        this.loadKennels()
    }

    render() {
        const {kennels} = this.state;
        const {kennelsListClass} = this.state;
        const {registered_user} = this.state;
        const {next} = this.state;

        return (
            <div>
                {registered_user === true ? <Link className='mr-2' maintainScrollPosition={false} to={{
                    pathname: '/kennels/create',
                    state: {fromDashboard: false}
                }}>Create kennel or cattery</Link> : ""}
                <button onClick={this.toggleKennelListClass}>Toggle class</button>

                {kennels.length > 0 ? kennels.map((kennelItem, index) => {
                    return (
                        <KennelInList kennel={kennelItem} elClass={kennelsListClass}/>
                    )
                }) : <p>No kennels found</p>}
                {next !== null && next !== undefined ?
                    <button onClick={this.loadMoreKennels}>Load more kennels</button> : ""}
            </div>
        );
    }
}

export default Kennels;
