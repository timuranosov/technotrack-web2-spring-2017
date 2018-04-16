import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {MenuItem, Nav, Navbar, NavDropdown, NavItem} from 'react-bootstrap';
import Avatar from 'material-ui/Avatar';


class NavBarTop extends Component {
    render() {
        return (
            <Navbar inverse collapseOnSelect>
                <Navbar.Header>
                    <Navbar.Brand>
                        <a href="/">MySocialNet</a>
                    </Navbar.Brand>
                    <Navbar.Toggle/>
                </Navbar.Header>
                <Navbar.Collapse>
                    <Nav>
                        <NavItem eventKey={1} href="#">Link 1</NavItem>
                        <NavItem eventKey={2} href="#">Link 2</NavItem>
                        <NavDropdown eventKey={3} title="Dropdown" id="basic-nav-dropdown">
                            <MenuItem eventKey={3.1}>Action 1</MenuItem>
                            <MenuItem eventKey={3.2}>Action 2</MenuItem>
                            <MenuItem eventKey={3.3}>Action 3</MenuItem>
                        </NavDropdown>
                    </Nav>
                    <Nav pullRight>
                        <NavItem eventKey={1} href="#">{this.props.user.username}</NavItem>
                        <Avatar src="../static/avatar.jpg" size={50}/>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        );
    }
}

NavBarTop.propTypes = {
    user: PropTypes.shape.isRequired({
        pk: PropTypes.number,
        username: PropTypes.string,
        avatar: PropTypes.string,
        first_name: PropTypes.string,
        last_name: PropTypes.string,
    }),
};


export default NavBarTop;
