import React, {ChangeEvent, FC, FormEvent, useState} from 'react'
import {Comment} from '../../types'
import css from './CommentsList.module.css'
import PseudoLink from "../PseudoLink/PseudoLink";
import {CommentsList} from "./CommentsList";
import {CommentForm} from "../CommentForm/CommentForm";


interface Props {
    comment: Comment
}

export const CommentRow: FC<Props> = ({comment,}) => {
    const [children, setChildren] = useState<Comment[]>(comment.children || [])
    const [activeReply, setActiveReply] = useState(false);
    const handleReplyClick = () => {
        setActiveReply(!activeReply);
    };

    const handleSubmit = (comment: Comment) => {
        setChildren([...children, comment]);
        setActiveReply(false);
    }

    const handleCancel = () => {
        setActiveReply(false);
    }


    return (
        <li className={css.item}>
                {comment.author.photoURL
                    ? <img className={css.icon} src={comment.author.photoURL} alt="profile picture" />
                    : <div className={css.icon} />
                }
                <div className={css.body}>
                    <div className={css.content}>
                        <div className={css.header}>
                            <div className={css.author}>{comment.author.name}</div>
                            <div className={css.date}>{comment.date}</div>
                        </div>
                        <p className={css.text}>{comment.text}</p>
                        <div className={css.action}>
                            <PseudoLink onClick={handleReplyClick}>reply</PseudoLink>
                        </div>
                        {activeReply && (
                            <div className={css.form}>
                                <CommentForm onSubmit={handleSubmit} onCancel={handleCancel} parentID={comment.id} />
                            </div>

                        )}
                     </div>
                    {children && (
                        <CommentsList comments={children} />
                    )}
                </div>
        </li>
    );
}
