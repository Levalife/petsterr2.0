import React, {Component} from 'react'
import {Link} from 'react-router-dom'
import cookie from "react-cookies";
import 'whatwg-fetch'

import KennelForm from './KennelForm'

class KennelDetail extends Component {
    constructor(props) {
        super(props);
        this.handleKennelItemUpdate = this.handleKennelItemUpdate.bind(this);
        this.state = {
            slug: null,
            kennel: null,
            doneLoading: false
        }
    }

    handleKennelItemUpdate(kennelItemData) {
        console.log('kennelItemData ', kennelItemData);
        this.setState({
            kennel: kennelItemData
        });
    }

    loadKennels(slug) {
        const endpoint = `/api/kennels/${slug}/`;
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
                if (response.status === 404) {
                    console.log('Page not found')
                }
                return response.json()
            }).then(function (responseData) {
            if (responseData.detail) {
                thisComp.setState({
                    doneLoading: true,
                    kennel: null
                })
            } else {
                thisComp.setState({
                    doneLoading: true,
                    kennel: responseData
                })
            }

        }).catch(function (error) {
            console.log("error", error)
        })
    }

    componentDidMount() {
        this.setState({
            slug: null,
            kennel: null
        });
        if (this.props.match) {
            const {slug} = this.props.match.params;
            this.setState({
                slug: slug,
                doneLoading: false,
            });
            this.loadKennels(slug);

        }
    }

    render() {
        const {doneLoading} = this.state;
        const {kennel} = this.state;
        return (
            <p>{(doneLoading === true) ?
                <div>
                    {kennel === null ? "Not found" :
                        // {kennel.owner === true ?
                            /*<Link className='mr-2'*/
                                  // maintainScrollPosition={false} to={{
                                // pathname: '/kennels/create',
                                // state: {fromDashboard: false}
                            // }}>Create</Link> : ""}
                        <div>
                        <h1>{kennel.title}</h1>
                        <p><label>Slug:</label> {kennel.slug}</p>
                        <p><label>Registration number:</label> {kennel.reg_number}</p>
                        <p><label>Skype:</label> {kennel.skype}</p>
                        <p><label>Site:</label> {kennel.site}</p>
                        <p><label>Facebook:</label> {kennel.facebook}</p>
                        <p>{kennel.about}</p>
                        <p><label>Country club:</label> {kennel.country_club}</p>

                        <p className='lead'><Link maintainScrollPosition={false} to={{
                        pathname: '/kennels',
                        state: {fromDashboard: false}
                    }}>
                        Kennels
                        </Link></p>

                        {kennel.owner === true ? <KennelForm kennel={kennel} kennelItemUpdated={this.handleKennelItemUpdate}/> : ""}
                        </div>
                    }

                </div> : 'Loading...'}</p>
        )
    }
}

export default KennelDetail