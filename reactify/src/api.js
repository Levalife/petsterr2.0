import axios from 'axios';
import cookie from 'react-cookies'

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

export default {
    user: {
                                // api requset return                               promise and then get request data
        login: (credentials) => axios.post('/api/v1/users/login/',
            { username: credentials.username, password: credentials.password }).then(res => res.data)
    }
}