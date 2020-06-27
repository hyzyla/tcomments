import React, {FC, useState} from 'react'
import {Comment} from '../../types'
import css from './CommentsList.module.css'
import {CommentRow} from "./CommentRow";
import {CommentForm} from "../CommentForm/CommentForm";

interface Props {
    comments: Comment[],
}

export const Comments: FC<Props> = ({comments: initComments}) => {
    const [comments, setComments] = useState<Comment[]>(initComments);

    const handleSubmit = (comment: Comment) => {
        setComments([comment, ...comments])
    };


    return (
        <>
            <CommentForm onSubmit={handleSubmit} />
            <ul className={css.list}>
                {comments.map(comment => {
                    return <CommentRow key={comment.id} comment={comment}/>
                })}
            </ul>
        </>
    );
};
