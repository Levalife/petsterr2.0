import React from 'react'
import PropTypes from 'prop-types';


const InlineErrors = ({ text }) => (
    <span style={{color: "#ae5856"}}>
        { text }
    </span>
);

InlineErrors.propTypes = {
    text: PropTypes.string.isRequired
};

export default InlineErrors;