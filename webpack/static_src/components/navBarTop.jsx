import React, {Component} from 'react';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';
import {Image, Nav, Navbar, NavItem} from 'react-bootstrap';

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
                        <NavItem eventKey={1} href="#">Link</NavItem>
                        <NavItem eventKey={2} href="#">Link</NavItem>
                    </Nav>
                    <Nav pullRight>
                        <NavItem eventKey={1} href="#">{this.props.profile.username}</NavItem>
                        <NavItem>
                            <Image width={35} height={35} src={this.props.profile.avatar} circle/>
                        </NavItem>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        );
    }
}


const mapStateToProps = state => ({
    profile: state.layout.account,
});

const mapDispatchToProps = distpatch => ({
    ...bindActionCreators({}, distpatch),
});

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(NavBarTop);
