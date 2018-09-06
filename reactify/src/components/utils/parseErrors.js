
import _ from 'lodash';

export default function (errors) {
    const result = [];
    _.forEach(errors, (val, key) => {
            result.push(val[0])
        });
    return result;
    
}