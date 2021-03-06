import React, {ChangeEvent, FC, FormEvent, useContext, useState} from 'react'
import {Comment} from '../../types'
import css from './CommentsList.module.css'
import PseudoLink from "../PseudoLink/PseudoLink";
import {CommentsList} from "./CommentsList";
import {CommentForm} from "../CommentForm/CommentForm";
import {UserIcon} from "../UserIcon/UserIcon";
import {currentUserContext} from "../PostPage/PostPage";


interface Props {
    comment: Comment
}

export const CommentRow: FC<Props> = ({comment,}) => {
    const [children, setChildren] = useState<Comment[]>(comment.children || []);
    const [activeReply, setActiveReply] = useState(false);
    const currentUser = useContext(currentUserContext);

    const handleReplyClick = () => {
        setActiveReply(!activeReply);
    };

    const handleSubmit = (comment: Comment) => {
        setChildren([...children, comment]);
        setActiveReply(false);
    };

    const handleCancel = () => {
        setActiveReply(false);
    };


    return (
        <li className={css.item}>
            <div className={css.sideBar}>
                <UserIcon user={comment.author}/>
                <div className={css.line}/>
            </div>
            <div className={css.body}>
                <div className={css.row}>
                <div className={css.content}>
                    <div className={css.header}>
                        <div className={css.author}>{comment.author.name}</div>
                    </div>
                    <div className={css.text}>
                        {comment.text.split('\n').map((line, idx) => {
                            return <p key={idx} className={css.paragraph}>{line}</p>;
                        })}
                    </div>
                </div>
                {currentUser && (
                    <div className={css.action}>
                        <PseudoLink onClick={handleReplyClick}>
                            <div className={css.reply}>
                                Reply
                            </div>
                        </PseudoLink>
                    </div>
                )}
                {activeReply && (
                    <div className={css.form}>
                        <CommentForm onSubmit={handleSubmit} onCancel={handleCancel} parentID={comment.id}/>
                    </div>
                )}
                </div>

                {children && (
                    <CommentsList comments={children}/>
                )}
            </div>
        </li>
    );
};
