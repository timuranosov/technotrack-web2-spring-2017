import React, { Component } from 'react';
import { Col, Nav, NavItem } from 'react-bootstrap';

class NavBarLeft extends Component {
  render() {
    return (
      <Col xs={4} md={2}>
        <Nav bsStyle="pills" stacked>
          <NavItem active eventKey="mypage">
            Моя страница
          </NavItem>
          <NavItem eventKey="feed">
            Лента
          </NavItem>
          <NavItem eventKey="chats">
            Сообщения
          </NavItem>
          <NavItem eventKey="friends">
            Друзья
          </NavItem>
          <NavItem eventKey="people">
            Поиск людей
          </NavItem>
        </Nav>
      </Col>
    );
  }
}

export default NavBarLeft;
