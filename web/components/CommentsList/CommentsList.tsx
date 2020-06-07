import React, { FC } from 'react'
import { Comment } from '../../types'
import css from './CommentsList.module.css'


interface Props {
    comments: Comment[]
}


export const CommentsList: FC<Props> = ({ comments }) => {
    if (comments.length === 0) {
        return null;
    }

    return (
        <ul className={css.list}>
            {comments.map(comment => {
                const children = comment.children;
                return (
                    <li key={comment.id} className={css.item}>
                        <div className={css.header}>
                            <div className={css.author}>{comment.author.name}</div>
                            <div className={css.date}>{comment.date}</div>
                        </div>
                        <p className={css.text}>{comment.text}</p>
                        {children && (
                            <div className={css.children}>
                                <CommentsList comments={children}/>
                            </div>
                        )}
                    </li>
                )
            })}
        </ul>
    );
};
