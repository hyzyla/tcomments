
import React, {FC} from "react";
import {User} from "../../types";
import css from "./UserIcon.module.css";

interface Props {
    user: User;
}

export const UserIcon: FC<Props> = ({ user }) => {
    return <div className={css.icon}>
        {user.photoURL &&
            <img className={css.icon} src={user.photoURL} alt="profile picture" />
        }
    </div>
}

