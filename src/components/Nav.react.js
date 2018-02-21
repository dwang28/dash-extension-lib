import React, {Component} from 'react';
import PropTypes from 'prop-types';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class Nav extends Component {
    render() {
        const {tag, id, className, href, children, datatoggle} = this.props;

        return (
            <nav id={id} class={className} href={href} data-toggle={datatoggle}>
                {tag}
                Hello 123
                {children}
            </nav>
        );
    }
}

Nav.propTypes = {
    tag: PropTypes.string,
    id: PropTypes.string,
    className: PropTypes.string,
    href: PropTypes.string,
    children: PropTypes.node,
    datatoggle: PropTypes.string

};
