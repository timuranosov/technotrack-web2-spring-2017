import React, {Component} from 'react';
import {ListItem} from 'material-ui/List';
import Divider from 'material-ui/Divider';
import {darkBlack} from 'material-ui/styles/colors';

export default class ChatComponent extends Component {
    render() {
        return (
            <div>
                <ListItem
                    primaryText="Алексей Иванов"
                    secondaryText={
                        <p>
                            <span style={{color: darkBlack}}>Что делаешь на выходных?</span><br/>
                        </p>
                    }
                    secondaryTextLines={2}
                />
                <Divider inset/>
            </div>
        );
    }
}
